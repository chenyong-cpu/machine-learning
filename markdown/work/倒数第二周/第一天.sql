-- 小程序、APP、公众号扩充有车用户

-- 构建一个月表存储小程序、APP、公众号的用户
-- 目前暂时存储最新一月的数据(7月份)
create table temp_car_user_month (
    label string, -- 小程序|APP|公众号
    name string, -- 程序名称
    bill_no string, -- 手机号
    month string -- 月份
) row format delimited fields terminated by ',' stored as orcfile;

-- 1. 将APP月表数据存入
insert into table temp_car_user_month
(
    select 'APP' as label, APP_NAME as name, BILL_NO as bill_no, '202207' as month
    from
    (
        select b.APP_NAME,a.BILL_NO
        from
        (
            select * from dwfu_hive_db.I_TNET_APP_USERS_M where P_MONTH=202207
        ) a
        inner join
        (
            select APP_CODE, case when APP_NAME like '%汽%修%' then '汽修'
            when  APP_NAME like '%修%车%' then '修车'
            when  APP_NAME like '%洗%车%' then '洗车'
            when  APP_NAME like '%保%养%' then '保养'
            when  APP_NAME like '%加%油%站%' then '加油站'
            else  APP_NAME end APP_NAME
            from default.D_CDM_APP_NAME_CODE where p_day=20220727 
            and (APP_NAME regexp '%汽%修%|%修%车%|%洗%车%|%保%养%|%加%油%站%'or APP_CODE in('D0990','42998','23018','39840','D1346','43753','43905','43906','D0723','D0089','D3961','D0954','39842','42999','D0861','D0908','D4188','25266','D0445','38824','25144','25520','42398','42417','22465','25519','25523','25518','22129','D0974','21851','28077','43476'))
        ) b
        on a.APP_CODE=b.APP_CODE
    ) t
    group by APP_NAME, BILL_NO
)

-- 2. 将微信公众号日存入
insert into table temp_car_user_month
(
    select '微信公众号' as label, article_title as name, bill_no, '202207' as month
    from
    (
        select b.article_title,a.BILL_NO
        from
        (
            select bill_no, MP_CODE from dwfu_hive_db.I_UNET_WEIXINMP_ACC_D where FLAG = 2 and P_DAY >= 20220701 and P_DAY < 20220801
        ) a
        inner join
        (
            select WEIXIN_MP_BIZ, case when article_title like '%汽%修%' then '汽修'
            when  article_title like '%修%车%' then '修车'
            when  article_title like '%洗%车%' then '洗车'
            when  article_title like '%保%养%' then '保养'
            when  article_title like '%加%油%站%' then '加油站'
            else  article_title end article_title
            from dwfu_hive_db.I_CDM_WEIXIN_ARTICLE_D where p_day=20220727 
            and (article_title like '%汽%修%' or article_title like '%修%车%' or article_title like '%洗%车%' or article_title like '%保%养%' or article_title like '%加%油%站%')
        ) b
        on a.MP_CODE=b.WEIXIN_MP_BIZ
    ) t 
    group by article_title, bill_no
)

-- 3. 将微信小程序日表存入
insert into table temp_car_user_month
(
    select '微信小程序' as label, name, bill_no, '202207' as month
    from
    (
        select b.name, a.bill_no from
        (
            select * from dwfu_hive_db.I_UNET_VISIT_WECHATAPPLET_D where P_DAY >= 20220701 and P_DAY < 20220801
        ) a
        inner join
        (
            select app_id, case when name like '%汽%修%' then '汽修'
            when name like '%修%车%' then '修车'
            when name like '%洗%车%' then '洗车'
            when name like '%保%养%' then '保养'
            when name like '%加%油%站%' then '加油站'
            else name end name
            from dwfu_hive_db.I_CDM_WECHATAPPLET
            where name like '%汽%修%' or name like '%修%车%' or name like '%洗%车%' or name like '%保%养%' or name like '%加%油%站%' or NAME like '易加油' or NAME like '易鑫车主服务' or NAME like '智慧U站车主版' or NAME like '汽车之家车主服务' or NAME like '小桔能源车主福利' or NAME like '滴滴顺风车车主注册' or NAME like '车主惠' or NAME like '瓜子车主服务' or NAME like '哈啰顺风车车主端' or NAME like '大昌车主会' or NAME like '车主查' or NAME like '智享汇车主服务' or NAME like '车主福利中心' or NAME like '易捷加油' or NAME like '团游官方号' or NAME like '石化加油' or NAME like '滴滴加油官方版本' or NAME like '小安加油' or NAME like '壳牌加油站' or NAME like '货车帮加油易车加油' or NAME like 'DT加油'
        ) b
        on a.APPLET_ID = b.APP_ID
    ) t
    group by name, bill_no
)

-- 筛选合格的手机号
-- 8307663
select count(distinct bill_no) 
from temp_car_user_month
where length(bill_no)=11 and substr(bill_no,1,1)=1 and bill_no regexp '1[0-9]{10}'

-- APP:5171774
-- 微信小程序:44487
-- 微信公众号:3751664

-- 获取有车一族7月份人数
select count(*) from sjwj_hive_db.L_BHV_TR_CAR_M where p_mon = '202207' and has_car = 1

-- 统计七天的数据量
select p_day, HOST, count(PHONE) CNT
from L_4S_HTTP_CARBRANDNAME_V2_D
where CARBRANDNAME is not null
group by p_day, HOST

select p_day, HOST, count(PHONE) CNT
from L_4S_HTTP_CARBRANDNAME_V2_D
where CARNAME is not null
group by p_day, HOST

select p_day, HOST, count(PHONE) CNT
from L_4S_HTTP_CARBRANDNAME_V2_D
where CARNAME2 is not null
group by p_day, HOST

-- 统计
select HOST, brand, sum(cnt) cnt
from
(
    select case when HOST like '%autoimg%' then '汽车之家' when HOST like '%bitautoimg%' then '易车' end HOST, case when CARBRANDNAME = '吉利' then '吉利' else '竞品' end brand , count(distinct PHONE) CNT
    from L_4S_HTTP_CARBRANDNAME_V2_D
    where CARBRANDNAME is not null
    group by HOST,  CARBRANDNAME
)
where HOST is not null
group by HOST, brand
-- 汽车之家	竞品	596710
-- 汽车之家	吉利	30115
-- 易车	竞品	612331


select HOST, brand, sum(cnt) cnt
from
(
    select case when HOST like '%autoimg%' then '汽车之家' when HOST like '%bitautoimg%' then '易车' end HOST,  case when CARNAME like '%缤瑞%' or CARNAME like '%缤越%' or CARNAME like '%博瑞%' or CARNAME like '%博越%' or CARNAME like '%帝豪%' or CARNAME like '%豪越%' or CARNAME like '%吉利%' or CARNAME like '%嘉际%' or CARNAME like '%星瑞%' or CARNAME like '%星越%' or CARNAME like '%远景%' then '吉利' else '竞品' end brand , count(distinct PHONE) CNT
    from L_4S_HTTP_CARBRANDNAME_V2_D
    where CARNAME is not null and HOST is not null
    group by HOST, CARNAME
)
where HOST is not null
group by HOST, brand
-- 汽车之家	吉利	7176
-- 汽车之家	竞品	19727
-- 易车	竞品	5

select HOST, brand, sum(cnt) cnt
from
(
    select case when HOST like '%autoimg%' then '汽车之家' when HOST like '%bitautoimg%' then '易车' end HOST,  case when CARNAME2 like '%缤瑞%' or CARNAME2 like '%缤越%' or CARNAME2 like '%博瑞%' or CARNAME2 like '%博越%' or CARNAME2 like '%帝豪%' or CARNAME2 like '%豪越%' or CARNAME2 like '%吉利%' or CARNAME2 like '%嘉际%' or CARNAME2 like '%星瑞%' or CARNAME2 like '%星越%' or CARNAME2 like '%远景%' then '吉利' else '竞品' end brand , count(distinct PHONE) CNT
    from L_4S_HTTP_CARBRANDNAME_V2_D
    where CARNAME2 is not null and HOST is not null
    group by HOST, CARNAME2
)
where HOST is not null
group by HOST, brand

-- 汽车之家	吉利	2525
-- 汽车之家	竞品	6869
-- 易车	吉利	32
-- 易车	竞品	98


------------------------------------------------------------
-- 导出七月使用吉利gnetlink APP的用户
create table temp_jili_july_car_82 as
select distinct bill_no from dwfu_hive_db.I_TNET_APP_USERS_M
WHERE p_month = '202207' AND app_code = '41382'

-- 导出七月使用吉利汽车的用户
insert into table temp_jili_july_car_82
(
    select distinct bill_no from dwfu_hive_db.I_TNET_APP_USERS_M
    WHERE p_month = '202207' AND app_code = '43477'
)

-- 导出七月使用吉利G-Netlink的用户
insert into table temp_jili_july_car_82
(
    select distinct bill_no from dwfu_hive_db.I_TNET_APP_USERS_M
    WHERE p_month = '202207' AND app_code = '43478'
)

select count(distinct bill_no) from dwfu_hive_db.I_TNET_APP_USERS_M
where p_month = '202206' and app_code in ('41382', '43477', '43478')

-- select count(distinct bill_no) from temp_jili_july_car_82
-- 409313

-- 用获取小程序、微信公众号、APP相关的代码与吉利APP7月用户关联判断人数
select count(distinct a.bill_no)
from temp_car_user_month a
inner join temp_jili_july_car_82 b
on a.bill_no = b.bill_no
-- 109026

-- 七月全部人口关联查看人数
select count(distinct a.bill_no)
from (
    select bill_no from dwfu_hive_db.I_TPOS_ADDRESS_GRID_M
    where p_mon = '202207'
) a
inner join temp_jili_july_car_82 b
on a.bill_no = b.bill_no
-- 407789

-- 关联6月份有车一族一族月表（因为7月份的还没有出来）
select count(distinct a.bill_no)
from (
    select bill_no from sjwj_hive_db.L_BHV_TR_CAR_M
    where p_mon = '202206' and has_car = 1
) a
inner join temp_jili_july_car_82 b
on a.bill_no = b.bill_no
-- 98840



-----------------------------------------------------------------
-- 由于有车一族只有6月的数据，因此以上的比较通通都要改为6月数据进行比较
-----------------------------------------------------------------

-- 6月使用吉利汽车APP人数：310149

-- 6月公众号、微信小程序、APP使用人数
-- 去重人数：9920447
-- 与吉利汽车APP用户关联人数：80643

-- 6月有车一族人数
-- 去重人数：15003379
-- 与吉利汽车APP用户关联人数：64802

-- 6月工作地居住地人口
-- 去重人数：96130389
-- 与吉利汽车APP用户关联人数：308726

-- 6月公众号、微信小程序、APP与有车一族重合人数：4834522
-- 6月公众号、微信小程序、APP与有车一族吉利APP用户重合人数：31154

-----------------------------------------------------------------
