select uri, p_hour, msisdn, HOST
from default.D_ENS_HTTP_4G_HIS
where p_hour = '2022080212' and HOST = 'hzxkctk.cn' and msisdn > 10000000000 and msisdn < 20000000000

select b.article_title,a.BILL_NO from
(
    select bill_no, MP_CODE from dwfu_hive_db.I_UNET_WEIXINMP_ACC_D where FLAG = 2 andP_DAY>= 20220701 and P_DAY < 20220801
) a
inner join
(
    select WEIXIN_MP_BIZ, article_title
    from dwfu_hive_db.I_CDM_WEIXIN_ARTICLE_D where p_day=20220727 
    and article_title in ('杭州摇号查询', '杭州摇号查询小助手', '杭州出行早知道')
) b
on a.MP_CODE=b.WEIXIN_MP_BIZ

select b.name, a.bill_no from
(
    select * from dwfu_hive_db.I_UNET_VISIT_WECHATAPPLET_D where P_DAY >= 20220701 andP_DAY < 20220801
) a
inner join
(
    select app_id, name
    from dwfu_hive_db.I_CDM_WECHATAPPLET
    where name in ('小客车车牌摇号', '杭州摇号助手'， '杭州车牌中签摇号查询', '汽车车牌摇号竞拍查询+', '小汽车车牌摇号', '小汽车车牌摇号查询', '汽车摇号中签查询', '小客车摇号结果查詢')
) b
on a.APPLET_ID = b.APP_ID