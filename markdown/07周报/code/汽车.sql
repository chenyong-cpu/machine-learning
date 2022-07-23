create table temp_l_attr_buycar_m_202206 as 
select user_id
,bill_no
,city_id
,county_id
,sex_new
,age
,p_mon
from dwfu_hive_db.A_USOC_USER_ATTR_m
where cust_state=2
and PROD_CATALOG_ID=1
and USER_STATE=1
and USER_TYPE=1
and p_mon='202206'
and substr(bill_no,1,1)=1
and length(bill_no)=11
and PLAN_TYPE IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,31,43,44,45,46)
group by user_id,bill_no,city_id,county_id,sex_new,age,p_mon
;

create table temp_l_attr_buycar_m_202206_01 as
select a1.user_id,a1.bill_no,a1.city_id,a1.county_id,a1.sex_new,a1.age,a1.p_mon from 
(select user_id,bill_no,city_id,county_id,sex_new,age,p_mon from temp_l_attr_buycar_m_202206) a1
left join 
(select bill_no
from sjwj_hive_db.l_attr_user_base_info_m
where p_mon='202206'
and has_car=1) a2
on a1.bill_no=a2.bill_no
where a2.bill_no is null
;

create table temp_l_attr_buycar_m_202206_02 as
select t1.* from
temp_szh_4s_yuce_result t1
left join
(
    select bill_no from temp_l_attr_buycar_m_202206_01
) t2
on t1.bill_no = t2.bill_no
where t2.bill_no is null

select count(*) from 
(select * from temp_l_attr_buycar_m_202206_02 where predflag = 1) t1
left join
(
    select bill_no
    from sjwj_hive_db.l_attr_user_base_info_m
    where p_mon='202206'
    and has_car=0
) t2
on t1.bill_no = t2.bill_no
where t2.bill_no is not null

-- 获取吉利APP的编号
create table temp_jili_20220715 as
select * from default.D_CDM_APP_NAME_CODE
where p_day='20220714' and (app_name like '%GKUI%' or app_name like '%吉利%')

app_name	app_classify_type	app_code	remark	p_day
北京吉利学院	教育	38922		20220714
吉利gnetlink	生活服务	41382		20220714
吉利汽车	生活服务	43477		20220714
吉利G-Netlink	生活服务	43478		20220714

--关联APP_USERS_M获取使用了该APP的用户
create table temp_jili_20220715_May as
SELECT * FROM dwfu_hive_db.I_TNET_APP_USERS_M
WHERE p_month = '202205' AND
app_code in ('41382', '43477', '43478')

-- 导出六月使用吉利gnetlink APP的用户
create table temp_jili_june_gnetlink as
select distinct bill_no from dwfu_hive_db.I_TNET_APP_USERS_M
WHERE p_month = '202206' AND
app_code = '41382'

-- 导出六月使用吉利汽车的用户
create table temp_jili_june_car as
select distinct bill_no from dwfu_hive_db.I_TNET_APP_USERS_M
WHERE p_month = '202206' AND
app_code = '43477'

-- 导出六月使用吉利G-Netlink的用户
create table temp_jili_june_Gnetlink as
select distinct bill_no from dwfu_hive_db.I_TNET_APP_USERS_M
WHERE p_month = '202206' AND
app_code = '43478'

-- 有车一族中吉利用户
create table temp_jili_20220715_User as
SELECT t1.*, t2.stay_days, t2.work_days, t2.stay_city_name, t2.work_city_name, t2.has_car, t2.car_probabi FROM temp_jili_20220715_May t1
inner join temp_has_car_last t2
on t1.bill_no = t2.bill_no

-- 使用常驻5月的数据
create table temp_jili_20220715_User_Stay as
SELECT t1.* FROM temp_jili_20220715_May t1
inner join (select * from dwfu_hive_db.I_TPOS_ADDRESS_GRID_M where p_mon = '202205') t2
on t1.bill_no = t2.bill_no

-- 使用汽车之家的手机号码
31497
create table temp_jili_20220715_CarHome as
SELECT t1.* FROM temp_jili_20220715_User_Stay t1
join (
	SELECT * FROM dwfu_hive_db.I_TNET_APP_USERS_M
	WHERE p_month = '202205' AND app_code = 'D0151'
	) t2
on t1.bill_no = t2.bill_no

---- 又是水的一天 ----

-- 杭州市202101-202205人口变化图
SELECT 月份, SUM(总人口数) 总人口数, SUM(常住人口数) 常住人口数, SUM(流动人口数) 流动人口数 FROM 杭州市
GROUP BY 月份

-- 杭州市202101-202205年龄段人口变化图
SELECT 月份, SUM(Age_0_17) Age_0_17, SUM(Age_18_29) Age_18_29, SUM(Age_30_39) Age_30_39, SUM(Age_40_49) Age_40_49, SUM(Age_50_59) Age_50_59, SUM(Age_60_69) Age_60_69, SUM(Age_70以上) Age_70以上 FROM 杭州市
GROUP BY 月份

-- 2021年杭州市各年龄段人口平均占比
select sum(a.Age_0_17) / 12 Age_0_17, sum(a.Age_18_29) / 12 Age_18_29, sum(a.Age_30_39) / 12 Age_30_39, sum(a.Age_40_49) / 12 Age_40_49, sum(a.Age_50_59) / 12 Age_50_59, sum(a.Age_60_69) / 12 Age_60_69, sum(a.Age_70以上) / 12 Age_70以上
from (
    SELECT 月份, SUM(Age_0_17) Age_0_17, SUM(Age_18_29) Age_18_29, SUM(Age_30_39) Age_30_39, SUM(Age_40_49) Age_40_49, SUM(Age_50_59) Age_50_59, SUM(Age_60_69) Age_60_69, SUM(Age_70以上) Age_70以上 FROM 杭州市
    WHERE 年份 = 2021
    GROUP BY 月份
) a

-- 2021年杭州市各省份人口每月平均数
select sum(a.北京) / 12 北京, sum(a.天津) / 12 天津, sum(a.河北) / 12 河北, sum(a.山西) / 12 山西, sum(a.内蒙) / 12 内蒙, sum(a.辽宁) / 12 辽宁, sum(a.吉林) / 12 吉利, sum(a.黑龙江) / 12 黑龙江, sum(a.上海) / 12 上海, sum(a.江苏) / 12 江苏, sum(a.浙江) / 12 浙江, sum(a.安徽) / 12 安徽, sum(a.福建) / 12 福建, sum(a.江西) / 12 江西, sum(a.山东) / 12 山东, sum(a.河南) / 12 河南, sum(a.湖北) / 12 湖北, sum(a.湖南) / 12 湖南, sum(a.广东) / 12 广东, sum(a.广西) / 12 广西, sum(a.海南) / 12 海南, sum(a.重庆) / 12 重庆, sum(a.四川) / 12 四川, sum(a.贵州) / 12 贵州, sum(a.云南) / 12 云南, sum(a.西藏) / 12 西藏, sum(a.陕西) / 12 陕西, sum(a.甘肃) / 12 甘肃, sum(a.青海) / 12 青海, sum(a.宁夏) / 12 宁夏, sum(a.新疆) / 12 新疆, sum(a.台湾) / 12 台湾, sum(a.香港) / 12 香港, sum(a.澳门) / 12 澳门 from 杭州市
from (
    select sum(北京) 北京, sum(天津) 天津, sum(河北) 河北, sum(山西) 山西, sum(内蒙) 内蒙, sum(辽宁) 辽宁, sum(吉林) 吉利, sum(黑龙江) 黑龙江, sum(上海) 上海, sum(江苏) 江苏, sum(浙江) 浙江, sum(安徽) 安徽, sum(福建) 福建, sum(江西) 江西, sum(山东) 山东, sum(河南) 河南, sum(湖北) 湖北, sum(湖南) 湖南, sum(广东) 广东, sum(广西) 广西, sum(海南) 海南, sum(重庆) 重庆, sum(四川) 四川, sum(贵州) 贵州, sum(云南) 云南, sum(西藏) 西藏, sum(陕西) 陕西, sum(甘肃) 甘肃, sum(青海) 青海, sum(宁夏) 宁夏, sum(新疆) 新疆, sum(台湾) 台湾, sum(香港) 香港, sum(澳门) 澳门 from 杭州市
    where 年份 = 2021
    group by 月份
) a

-- 202101-202205杭州市各省份人口变化
select 月份, sum(浙江) 浙江, sum(北京) 北京, sum(天津) 天津, sum(河北) 河北, sum(山西) 山西, sum(内蒙) 内蒙, sum(辽宁) 辽宁, sum(吉林) 吉利, sum(黑龙江) 黑龙江, sum(上海) 上海, sum(江苏) 江苏, sum(安徽) 安徽, sum(福建) 福建, sum(江西) 江西, sum(山东) 山东, sum(河南) 河南, sum(湖北) 湖北, sum(湖南) 湖南, sum(广东) 广东, sum(广西) 广西, sum(海南) 海南, sum(重庆) 重庆, sum(四川) 四川, sum(贵州) 贵州, sum(云南) 云南, sum(西藏) 西藏, sum(陕西) 陕西, sum(甘肃) 甘肃, sum(青海) 青海, sum(宁夏) 宁夏, sum(新疆) 新疆, sum(台湾) 台湾, sum(香港) 香港, sum(澳门) 澳门 from 杭州市
group by 月份

--
select 区县, sum(总人口数), sum(常住人口数), sum(流动人口数)
from 杭州市
where 年份 = 2021
group by 区县
