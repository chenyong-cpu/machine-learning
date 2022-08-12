-- 4S店的位置
create table temp_szh_jili_use_app_7_0 as
select 
case when poi_name like '%吉利%' then '吉利'
            when poi_name like '%长安%' then '长安'
            when poi_name like '%长城%' then '长城'
            when poi_name like '%星途%' then '星途'
            when poi_name like '%上汽%' then '上汽'
            when poi_name like '%广汽%' then '广汽'
            when poi_name like '%东风%' then '东风'
            when poi_name like '%丰田%' then '丰田'
            when poi_name like '%北京%' then '北京'
            when poi_name like '%奇瑞%' then '奇瑞'
            when poi_name like '%一汽%' then '一汽'
            when poi_name like '%领克%' then '领克'
            when poi_name like '%马自%' then '马自'
            when poi_name like '%比亚%' then '比亚'
            when poi_name like '%大众%' then '大众'
            when poi_name like '%荣威%' then '荣威'
            when poi_name like '%威马%' then '威马'
            when poi_name like '%几何%' then '几何'
            when poi_name like '%五菱%' then '五菱'
            when poi_name like '%宝骏%' then '宝骏'
            when poi_name like '%哈弗%' then '哈弗'
            when poi_name like '%雪佛%' then '雪佛'
            when poi_name like '%捷达%' then '捷达'
            when poi_name like '%哪吒%' then '哪吒'
            when poi_name like '%现代%' then '现代'
            when poi_name like '%本田%' then '本田'
            when poi_name like '%奔腾%' then '奔腾'
            when poi_name like '%别克%' then '别克'
            when poi_name like '%日产%' then '日产'
            when poi_name like '%福特%' then '福特'
            when poi_name like '%三菱%' then '三菱'
            when poi_name like '%红旗%' then '红旗'
            when poi_name like '%欧拉%' then '欧拉'
            when poi_name like '%雪铁%' then '雪铁'
            end brand
,poi_name
     ,bd_longitude as longitude
     ,bd_latitude as latitude
from dwfu_hive_db.I_UPOS_POI_M
where p_mon=202206
  and city_name <>''
  and poi_cls1 in ('4S服务','汽车销售')
  and poi_cls2 in ('4S店','','经销商','汽车销售')
  and poi_cls3 ='汽车销售'
  and poi_name regexp '吉利|长安|长城|星途|上汽|广汽|东风|丰田|北京|奇瑞|一汽|领克|马自|比亚|大众|荣威|威马|几何|五菱|宝骏|哈弗|雪佛|捷达|哪吒|现代|本田|奔腾|别克|日产|福特|三菱|红旗|欧拉|雪铁'

create table temp_szh_jili_use_app_7_1 as
select case  when poi_name like '%吉利%' then '吉利'
            when poi_name like '%长安%' then '长安'
            when poi_name like '%长城%' then '长城'
            when poi_name like '%星途%' then '星途'
            when poi_name like '%上汽%' then '上汽'
            when poi_name like '%广汽%' then '广汽'
            when poi_name like '%东风%' then '东风'
            when poi_name like '%丰田%' then '丰田'
            when poi_name like '%北京%' then '北京'
            when poi_name like '%奇瑞%' then '奇瑞'
            when poi_name like '%一汽%' then '一汽'
            when poi_name like '%领克%' then '领克'
            when poi_name like '%马自%' then '马自'
            when poi_name like '%比亚%' then '比亚'
            when poi_name like '%大众%' then '大众'
            when poi_name like '%荣威%' then '荣威'
            when poi_name like '%威马%' then '威马'
            when poi_name like '%几何%' then '几何'
            when poi_name like '%五菱%' then '五菱'
            when poi_name like '%宝骏%' then '宝骏'
            when poi_name like '%哈弗%' then '哈弗'
            when poi_name like '%雪佛%' then '雪佛'
            when poi_name like '%捷达%' then '捷达'
            when poi_name like '%哪吒%' then '哪吒'
            when poi_name like '%现代%' then '现代'
            when poi_name like '%本田%' then '本田'
            when poi_name like '%奔腾%' then '奔腾'
            when poi_name like '%别克%' then '别克'
            when poi_name like '%日产%' then '日产'
            when poi_name like '%福特%' then '福特'
            when poi_name like '%三菱%' then '三菱'
            when poi_name like '%红旗%' then '红旗'
            when poi_name like '%欧拉%' then '欧拉'
            when poi_name like '%雪铁%' then '雪铁'
            end brand
,poi_name
     ,longitude
     ,latitude
from dwfu_hive_db.i_uidct_all_trail_mr_d
where poi_cls1_code='009'
  and stay_duration>15*60
  and poi_cls3 regexp '吉利|长安|长城|星途|上汽|广汽|东风|丰田|北京|奇瑞|一汽|领克|马自|比亚|大众|荣威|威马|几何|五菱|宝骏|哈弗|雪佛|捷达|哪吒|现代|本田|奔腾|别克|日产|福特|三菱|红旗|欧拉|雪铁'
and chan_name='百度POI'
and p_day=20220729
group by poi_name
        ,longitude
        ,latitude

create table temp_szh_jili_use_app_7_2 as
select brand
,sales_point as poi_name
       ,longtitude
       ,latitude
from temp_szh_jili_use_app_5
where brand regexp '吉利|长安|长城|星途|上汽|广汽|东风|丰田|北京|奇瑞|一汽|领克|马自|比亚|大众|荣威|威马|几何|五菱|宝骏|哈弗|雪佛|捷达|哪吒|现代|本田|奔腾|别克|日产|福特|三菱|红旗|欧拉|雪铁'

create table temp_szh_jili_use_app_7_3 as
select brand
,sales_point as poi_name
     ,longtitude
     ,latitude
from temp_szh_jili_use_app_6
where brand regexp '吉利|长安|长城|星途|上汽|广汽|东风|丰田|北京|奇瑞|一汽|领克|马自|比亚|大众|荣威|威马|几何|五菱|宝骏|哈弗|雪佛|捷达|哪吒|现代|本田|奔腾|别克|日产|福特|三菱|红旗|欧拉|雪铁'


create table temp_szh_jili_use_app_7 as
    select brand,poi_name
         ,cast(floor((longitude-0.000441)/(0.00045)) as string) lng_join
         ,cast(floor((latitude-0.000381)/(0.00045)) as string) lat_join
from(
select brand,poi_name,longitude,latitude,row_number()over(partition by poi_name order by poi_name)rn
from(
select brand,poi_name,longitude,latitude 
from temp_szh_jili_use_app_7_0
union all
select brand,poi_name,longitude,latitude 
from temp_szh_jili_use_app_7_1
union all
(
    select brand,poi_name,longtitude as longitude,latitude 
    from temp_szh_jili_use_app_7_2
)
union all
(
    select brand,poi_name,longtitude as longitude,latitude 
    from temp_szh_jili_use_app_7_3
)
)a
)b where rn = 1

-- 4S店的位置地市
create table temp_szh_jili_use_app_8 as
select a.poi_name,a.brand,concat(a.lng_join,'_',a.lat_join) grid_id,b.city_id
from temp_szh_jili_use_app_7 a
left join (select lng_join,lat_join,city_id from dwfu_hive_db.I_CDM_GRID2COMMUNITY) b
on a.lng_join = b.lng_join and a.lat_join = b.lat_join

create table temp_szh_jili_use_app_9_0 as
select bill_no,o_grid_id as grid_id,P_DAY,p_city
from dwfu_hive_db.I_TPOS_MR_OD_TRACE_D
where P_DAY>=20220701 and P_DAY<20220711 and hour(o_in_time)>=9 and hour(o_out_time)<19 and o_stay_duration> 600 and o_stay_duration < 18000
union
select bill_no,d_grid_id as grid_id,P_DAY,p_city
from dwfu_hive_db.I_TPOS_MR_OD_TRACE_D
where P_DAY>=20220701 and P_DAY<20220711 and hour(d_in_time)>=9 and hour(d_out_time)<19 and d_stay_duration> 600 and d_stay_duration < 18000

create table temp_szh_jili_use_app_9_1 as
select bill_no,o_grid_id as grid_id,P_DAY,p_city
from dwfu_hive_db.I_TPOS_MR_OD_TRACE_D
where P_DAY>=20220711 and P_DAY<20220721 and hour(o_in_time)>=9 and hour(o_out_time)<19 and o_stay_duration> 600 and o_stay_duration < 18000
    union
select bill_no,d_grid_id as grid_id,P_DAY,p_city
from dwfu_hive_db.I_TPOS_MR_OD_TRACE_D
where P_DAY>=20220711 and P_DAY<20220721 and hour(d_in_time)>=9 and hour(d_out_time)<19 and d_stay_duration> 600 and d_stay_duration < 18000

create table temp_szh_jili_use_app_9_2 as
select bill_no,o_grid_id as grid_id,P_DAY,p_city
from dwfu_hive_db.I_TPOS_MR_OD_TRACE_D
where P_DAY>=20220721 and P_DAY<20220801 and hour(o_in_time)>=9 and hour(o_out_time)<19 and o_stay_duration> 600 and o_stay_duration < 18000
    union
select bill_no,d_grid_id as grid_id,P_DAY,p_city
from dwfu_hive_db.I_TPOS_MR_OD_TRACE_D
where P_DAY>=20220721 and P_DAY<20220801 and hour(d_in_time)>=9 and hour(d_out_time)<19 and d_stay_duration> 600 and d_stay_duration < 18000

create table temp_szh_jili_use_app_10 as 
select bill_no,grid_id,P_DAY,p_city from temp_szh_jili_use_app_9_0
union all
select bill_no,grid_id,P_DAY,p_city from temp_szh_jili_use_app_9_1
union all
select bill_no,grid_id,P_DAY,p_city from temp_szh_jili_use_app_9_2


-- OD表到过4S店的一个月
create table temp_szh_jili_use_app_11 as
select  
a.brand
,a.poi_name
,a.grid_id
,b.P_DAY
,b.p_city
,b.bill_no
from temp_szh_jili_use_app_8 a
join temp_szh_jili_use_app_10 b
on a.grid_id=b.grid_id and a.city_id=b.p_city

--特征
1.一个月是否去过4S店
2.一个月去过几天
3.一个月去过几个4S店
4.一个月去过几次4S店
5.一个月是否跨地市去4S店
6.最近一个周是否去过4S店
7.最近一个周去过几天
8.最近一个周去过几个4S店
9.最近一个周去过几次4S店
10.最近一个周是否跨地市去4S店

create table temp_szh_jili_use_app_12 as
select BILL_NO,if(sum(mon_is_get_4s)>0,1,0)mon_is_get_4s,mon_day_cnt,mon_cnt1
sum(mon_cnt2)mon_cnt2,mon_is_get_city
from(
select BILL_NO,mon_is_get_4s
,count(P_DAY)over(partition by BILL_NO, P_DAY) mon_day_cnt
,count(poi_name)over(partition by BILL_NO, poi_name) mon_cnt1
,count(poi_name)over(partition by BILL_NO,P_DAY, poi_name) mon_cnt2
,sum(mon_is_get_city)over(partition by BILL_NO) mon_is_get_city
,P_DAY
from (
select a.BILL_NO
,if(b.brand is null,0,1) mon_is_get_4s
,if(a.HOME_CITY_ID<>b.p_city and a.WORK_CITY_ID<>b.p_city,1,0) mon_is_get_city
,b.brand,b.poi_name,b.grid_id,b.P_DAY,b.p_city
from temp_szh_jili_use_app_4 a
left join temp_szh_jili_use_app_11 b
on a.BILL_NO = b.bill_no)c)d 
group by BILL_NO,mon_day_cnt,mon_cnt1,mon_is_get_city

create table temp_szh_jili_use_app_13 as
select BILL_NO,if(sum(week_is_get_4s)>0,1,0) week_is_get_4s,week_day_cnt,week_cnt1,sum(week_cnt2)week_cnt2,week_is_get_city
from(
select BILL_NO,week_is_get_4s
,count(P_DAY)over(partition by BILL_NO, P_DAY) week_day_cnt
,count(poi_name)over(partition by BILL_NO, poi_name) week_cnt1
,count(poi_name)over(partition by BILL_NO,P_DAY, poi_name) week_cnt2
,sum(week_is_get_city)over(partition by BILL_NO) week_is_get_city
,P_DAY
from (
select a.BILL_NO
,if(b.brand is null,0,1) week_is_get_4s
,if(a.HOME_CITY_ID<>b.p_city and a.WORK_CITY_ID<>b.p_city,1,0) week_is_get_city
,b.brand,b.poi_name,b.grid_id,b.P_DAY,b.p_city
from temp_szh_jili_use_app_4 a
left join (select * from temp_szh_jili_use_app_11 where P_DAY>20220722) b
on a.BILL_NO = b.bill_no)c)d 
group by BILL_NO,week_is_get_4s,week_day_cnt,week_cnt1,week_is_get_city

-- 是否去过4S特征
create table temp_szh_jili_use_app_14 as
select a.BILL_NO,a.HOME_CITY_ID,a.HOME_CITY_NAME,a.WORK_CITY_ID,a.WORK_CITY_NAME
,a.opp_number,a.call_tot_dur,a.call_tot_cnt,a.contact_rate
,b.mon_is_get_4s,b.mon_day_cnt,b.mon_cnt1
,b.mon_cnt2,b.mon_is_get_city
,c.week_is_get_4s,c.week_day_cnt,c.week_cnt1
,c.week_cnt2,c.week_is_get_city
from 
temp_szh_jili_use_app_4 a
left join temp_szh_jili_use_app_12 b
on a.BILL_NO =b.BILL_NO
left join temp_szh_jili_use_app_13 c
on a.BILL_NO =c.BILL_NO

create table temp_szh_jili_use_app_15 as
select BILL_NO
,if(sum(is_get1)>0 or sum(is_get2)>0 or sum(is_get3)>0,1,0)is_get
,sum(is_get1)is_get1
,count(distinct carbrandname)carbrandname
,sum(is_get2)is_get2
,count(distinct carname)carname
,sum(is_get3)is_get3
,count(distinct carname2)carname2
from(
select a.BILL_NO,if(b.carbrandname is not null,1,0)is_get1,b.carbrandname,if(b.carname is not null,1,0)is_get2,b.carname,if(b.carname2 is not null,1,0)is_get3,b.carname2,b.p_day
from temp_szh_jili_use_app_4 a
left join(
select carbrandname,carname,carname2,phone,p_day
from L_4S_HTTP_CARBRANDNAME_V2_D 
where P_DAY>= 20220701 and P_DAY<20220801 and host like '%autohome%')b
on a.BILL_NO=b.phone)a group by BILL_NO

-- 收入水平等级月模型 L_ATTR_INCOME_LEVEL_M
create table temp_szh_jili_use_app_16 as
select a.BILL_NO,a.HOME_CITY_ID,a.HOME_CITY_NAME,a.WORK_CITY_ID,a.WORK_CITY_NAME
,a.opp_number,a.call_tot_dur,a.call_tot_cnt,a.contact_rate
,a.mon_is_get_4s,a.mon_day_cnt,a.mon_cnt1
,a.mon_cnt2,a.mon_is_get_city
,a.week_is_get_4s,a.week_day_cnt,a.week_cnt1
,a.week_cnt2,a.week_is_get_city
,b.is_get,b.is_get1,b.carbrandname
,b.is_get2,b.carname,b.is_get3,b.carname2
,c.FEE_SCORE,c.COMMUNITY_LEVEL_SCORE,c.APP_SCORE
,c.TRAVEL_SCORE,c.FINANCIAL_SCORE,c.FUND_SCORE
,c.EDU_SCORE,c.OCCU_SCORE,c.INCOME_SCORE
,c.FINAL_INCOME_SCORE,c.INCOME_LEVEL
,d.ISMARR,d.HAVEOLD,d.FERTILE,d.FAMSTRU,d.OCCU
,d.SUB_OCCU_NAME,d.IF_EXECUTIVE,d.IF_BUSINESS
,d.IF_SALARIAT,d.MIGRANT_WORKER_P
from temp_szh_jili_use_app_14 a
left join
temp_szh_jili_use_app_15 b
on a.BILL_NO=b.BILL_NO
left join
(select PRODUCT_NO,FEE_SCORE,COMMUNITY_LEVEL_SCORE,APP_SCORE
,TRAVEL_SCORE,FINANCIAL_SCORE,FUND_SCORE,EDU_SCORE,OCCU_SCORE
,INCOME_SCORE,FINAL_INCOME_SCORE,INCOME_LEVEL 
from sjwj_hive_db.L_ATTR_INCOME_LEVEL_M where P_MON = 202206)c
on a.BILL_NO=c.PRODUCT_NO
left join
(select BILL_NO,ISMARR,HAVEOLD,FERTILE,FAMSTRU,OCCU,SUB_OCCU_NAME
,IF_EXECUTIVE,IF_BUSINESS,IF_SALARIAT,MIGRANT_WORKER_P
from sjwj_hive_db.L_ATTR_USER_BASE_INFO_M where P_MON = 202206)d
on a.BILL_NO=d.BILL_NO