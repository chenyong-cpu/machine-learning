--用户基本信息 ===> 获取用户的城市、年龄、性别、身份证、工作地居住地基站，经纬度这些数据
drop table if exists tmp_ryj_has_car_basic_user;
create table tmp_ryj_has_car_basic_user as
select t1.bill_no,t1.user_id,t1.city_id,t1.age,t1.sex,t1.cust_name,t1.card_type,t1.card_code, 
t1.work_lac_ci,t2.lac_ci_name work_lacci_name,t1.work_longitude,t1.work_latitude,
t1.stay_lac_ci,t3.lac_ci_name stay_lacci_name,
t1.stay_longitude,t1.stay_latitude,t1.work_stay_distance,t1.rest_days,t1.work_days
from (SELECT t1.bill_no,t1.user_id,t1.city_id,t1.age,t1.sex,t1.cust_name,t1.card_type,t1.card_code, 
t1.work_lac_ci,t1.work_longitude,t1.work_latitude,t1.stay_lac_ci,
t1.stay_longitude,t1.stay_latitude,t1.work_stay_distance,t1.rest_days,t1.work_days
       FROM dwfu_hive_db.a_tpos_stay_product_d T1
       where p_day='${curmlastday}'  
       and work_stay_distance is not null 
       )t1
left join dwfu_hive_db.i_cdm_lacci_zj t2 on t1.work_lac_ci=t2.lac_ci 
left join dwfu_hive_db.i_cdm_lacci_zj t3 on t1.stay_lac_ci=t3.lac_ci 
;

--上班距离 ===> 获取用户的工作地距离、工作天数等数据
drop table if exists tmp_ryj_has_car_work_distance;
create table tmp_ryj_has_car_work_distance as
select t.bill_no,t.user_id,avg(t.WORK_STAY_DISTANCE) WORK_STAY_DISTANCE,avg(t.REST_DAYS) REST_DAYS,avg(t.STAY_DAYS) STAY_DAYS,avg(t.WORK_DAYS) WORK_DAYS from 
(select	bill_no,user_id,work_latitude,stay_latitude,work_longitude,stay_longitude,WORK_STAY_DISTANCE,REST_DAYS,STAY_DAYS,WORK_DAYS
from DWFU_HIVE_DB.A_TPOS_STAY_PRODUCT_D   
where p_day >= '${mtaskid}01' and
p_day <=  '${curmlastday}'
and work_stay_distance is not null) t
group by t.bill_no,t.user_id;

-- 基站速度
drop table if exists tmp_ryj_has_car_lacci_speed;
create table tmp_ryj_has_car_lacci_speed as
select t1.bill_no,t1.cust_name,count(1) work_cnt,
concat(floor(avg(out_stime)/3600),':',floor(pmod(avg(out_stime),3600)/60),':',pmod(avg(out_stime),60)) out_stime_avg,
avg(out_stime)/60.0 out_stime_avg1,avg(back_stime)/60.0 back_stime_avg1,
std(out_stime) out_stime_std,
concat(floor(avg(back_stime)/3600),':',floor(pmod(avg(back_stime),3600)/60),':',pmod(avg(back_stime),60)) back_stime_avg,
std(back_stime) back_stime_std,
avg(time_tot) time_tot_avg,std(time_tot) time_tot_std,
avg(dis_tot ) dis_tot_avg,std(dis_tot ) dis_tot_std,
avg(max_speed ) max_speed_avg,std(max_speed) max_speed_std,
avg(min_speed ) min_speed_avg,std(min_speed ) min_speed_std,
avg(speed_avg ) speed_avg_avg,std(speed_avg ) speed_avg_std,
avg(speed_std ) speed_std_avg,std(speed_std ) speed_std_std,
avg(flux_tot ) flux_tot_avg,std(flux_tot ) flux_tot_std,
avg(visit_tot ) visit_tot_avg,std(visit_tot ) visit_tot_std,
avg(map_visit_cnt ) map_visit_cnt_avg,std(map_visit_cnt ) map_visit_cnt_std,
avg(app_cnt ) app_cnt_avg,std(app_cnt ) app_cnt_std,
avg(lacci_cnt ) lacci_cnt_avg,std(lacci_cnt ) lacci_cnt_std,
avg(atan_speed ) atan_speed_avg,std(atan_speed ) atan_speed_std,
avg(atan_app ) atan_app_avg,std(atan_app ) atan_app_std,
nvl(sum(is_subway),0)/count(1) subway_probabi
from (select hour(out_time)*3600+minute(out_time)*60+second(out_time) out_stime,hour(back_time)*3600+minute(back_time)*60+second(back_time) back_stime
 ,bill_no
,cust_name
,out_time
,back_time
,time_tot
,dis_tot
,max_speed
,min_speed
,speed_avg
,speed_std
,flux_tot
,visit_tot
,app_cnt
,map_visit_cnt
,map_app_cnt
,lacci_cnt
,subway_cnt
,atan_speed
,atan_app
,is_subway
,out_type
from sjwj_hive_db.l_bhv_tr_type_lacci_d where p_day between '${mtaskid}01' and '${curmlastday}'     
) t1
group by t1.bill_no,t1.cust_name;

--基站速度参数_月汇总tot ===> 估计是得出用户的移动速度进行分析判断
drop table if exists tmp_ryj_tr_type_lacci_tot;
create table tmp_ryj_tr_type_lacci_tot as
select t1.bill_no,t1.cust_name,t1.out_stime_avg,t1.back_stime_avg,t1.time_tot_avg,t1.dis_tot_avg, t1.speed_avg_avg,t1.flux_tot_avg,t1.app_cnt_avg,t1.lacci_cnt_avg,t1.subway_probabi,
atan(dis_tot_avg/10000+max_speed_avg/100+speed_std_avg/50+speed_avg_avg/100+out_stime_std/10000+back_stime_std/10000 )*2/pi() atan_speed,
atan(flux_tot_avg/102400+visit_tot_avg/100-map_visit_cnt_avg/100)*2/pi() atan_app
from tmp_ryj_has_car_lacci_speed t1;

--收入水平等属性 ===> 得出用户的收入水平
drop table if exists tmp_ryj_has_car_attr;
create table tmp_ryj_has_car_attr as
select bill_no,user_id,IF_EXECUTIVE,EXECUTIVE_SCORE,IF_BUSINESS,BUSINESS_SCORE,IF_SALARIAT,IF_MIGRANT_WORKER,MIGRANT_WORKER_P,INCOME_LEVEL,COMMUNITY_PRICE,COMMUNITY_LEVEL
from sjwj_hive_db.L_ATTR_USER_BASE_INFO_M
where p_mon='${lm_mtaskid}';

--汽车相关通话 ===> 汽车类相关通话次数
drop table if exists tmp_ryj_has_car_call;
create table tmp_ryj_has_car_call as
select t.user_id,t.bill_no,sum(CALL_CNT) call_cnt_tot,sum(CALL_DUR_M) call_dur_tot from
	(select a.user_id,a.bill_no,CALL_CNT,CALL_DUR_M,OPP_USER_NO
	from (SELECT a.user_id,a.bill_no,CALL_CNT,CALL_DUR_M,OPP_USER_NO 
	      FROM dwfu_hive_db.I_UPRD_CALL_OPP_M a
	      WHERE p_mon='${mtaskid}'
	      ) a
	inner join (select bill_no from sjwj_hive_db.L_CMM_DM_TR_PHONE WHERE p_mon='${mtaskid}') b
	on a.OPP_USER_NO=b.bill_no) t
group by t.user_id,t.bill_no;

-- 汽车相关APP使用 ===> 汽车类APP使用情况
drop table if exists tmp_ryj_has_car_app;
create table tmp_ryj_has_car_app as
select t.bill_no,count(1) app_cnt,sum(app_flux_tot)/1024/1024 flux_mb from
	(select bill_no,app_id,sum(up_flux+down_flux) app_flux_tot,sum(visit_cnt) visit_cnt_app,poi_name app_name,poi_cls2 app_classify_type
	from DWFU_HIVE_DB.I_UIDCT_ALL_APP_D
	where p_day >= '${l2m_mtaskid}01' 
     and  p_day <='${curmlastday}'
     and POI_CLS1_CODE='009'
	group by bill_no,app_id,poi_name,poi_cls2) t
group by t.bill_no;

-- 整合宽表
drop table if exists zqs_ryj_has_car_summary;
create table zqs_ryj_has_car_summary as
select a.bill_no,a.user_id,a.city_id,a.age,a.sex
		,b.WORK_STAY_DISTANCE,b.REST_DAYS,b.STAY_DAYS,b.WORK_DAYS
		,e.work_cnt,out_stime_avg1,out_stime_std,back_stime_avg1,back_stime_std,time_tot_avg,time_tot_std,dis_tot_avg,dis_tot_std,max_speed_avg,max_speed_std,min_speed_avg,min_speed_std
		,speed_avg_avg,speed_avg_std,speed_std_avg,speed_std_std,flux_tot_avg,flux_tot_std,visit_tot_avg,visit_tot_std,map_visit_cnt_avg,map_visit_cnt_std,app_cnt_avg,app_cnt_std
		,lacci_cnt_avg,lacci_cnt_std,atan_speed_avg,atan_speed_std,atan_app_avg,atan_app_std,subway_probabi		
		,f.call_cnt_tot,f.call_dur_tot
		,g.app_cnt
		,EXECUTIVE_SCORE,BUSINESS_SCORE,IF_SALARIAT,MIGRANT_WORKER_P,INCOME_LEVEL,COMMUNITY_PRICE,COMMUNITY_LEVEL
from tmp_ryj_has_car_basic_user a
left join tmp_ryj_has_car_work_distance b -- 工作距离
on a.bill_no=b.bill_no
left join tmp_ryj_has_car_lacci_speed e -- 移动速度
on a.bill_no=e.bill_no
left join tmp_ryj_has_car_attr c -- 收入水平
on a.bill_no=c.bill_no
left join tmp_ryj_has_car_call f -- 与车相关的通话
on a.bill_no=f.bill_no
left join tmp_ryj_has_car_app g -- 与车相关的APP
on a.bill_no=g.bill_no;

----3.挖掘模型信息 
--SJWJ_HIVE_DB.L_ATTR_USER_BASE_INFO_M     lm_mtaskid
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP2;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP2
AS
SELECT A.USER_ID
       ,A.BILL_NO
       ,CASE WHEN B.FAMSTRU IS NULL THEN 'unknown' ELSE B.FAMSTRU END AS FAMSTRU
       ,CASE WHEN B.OCCU    IS NULL THEN 'unknown' ELSE B.OCCU    END  AS  OCCU
       ,CASE WHEN B.SUB_OCCU_NAME    IS NULL THEN 'unknown'  else    B.SUB_OCCU_NAME     end as SUB_OCCU_NAME    
       ,CASE WHEN B.LIFE_STAGE       IS NULL THEN 'unknown'  else    B.LIFE_STAGE        end as LIFE_STAGE       
       ,CASE WHEN B.EXECUTIVE_SCORE  IS NULL THEN 0  else    B.EXECUTIVE_SCORE   end as EXECUTIVE_SCORE  
       ,CASE WHEN B.BUSINESS_SCORE   IS NULL THEN 0  else    B.BUSINESS_SCORE    end as BUSINESS_SCORE   
       ,CASE WHEN B.IF_SALARIAT      IS NULL THEN 'unknown' WHEN B.IF_SALARIAT = '1' THEN '工薪阶层' WHEN B.IF_SALARIAT = '0' THEN '非工薪阶层'  end as IF_SALARIAT      
       ,CASE WHEN B.INCOME_LEVEL  IS NULL THEN 0  else    B.INCOME_LEVEL      end as INCOME_LEVEL     
       ,CASE WHEN B.MIGRANT_WORKER_P IS NULL THEN 0  else    B.MIGRANT_WORKER_P  end as MIGRANT_WORKER_P 
       ,CASE WHEN B.EDU_LEVEL        IS NULL THEN 'unknown'  else    B.EDU_LEVEL         end as EDU_LEVEL        
FROM TEMP_L_BHV_TR_CAR_M_TMP1  A
LEFT JOIN (SELECT USER_ID
                  ,BILL_NO
                  ,FAMSTRU
                  ,OCCU
                  ,SUB_OCCU_NAME
                  ,LIFE_STAGE
                  ,EXECUTIVE_SCORE
                  ,BUSINESS_SCORE
                  ,IF_SALARIAT
                  ,INCOME_LEVEL
                  ,MIGRANT_WORKER_P
                  ,CAR_PROBABI
                  ,EDU_LEVEL
           FROM SJWJ_HIVE_DB.L_ATTR_USER_BASE_INFO_M
           WHERE P_MON='${lm_mtaskid}'
           )B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO

----4.常驻地 ===> 获取用户常住地信息
--DWFU_HIVE_DB.A_TPOS_STAY_PRODUCT_D  curmlastday
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP3;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP3
AS
SELECT A.USER_ID
      ,A.BILL_NO
      ,MAX(CASE WHEN B.STAY_CITY_NAME_NEW IS NOT NULL THEN B.STAY_CITY_NAME_NEW ELSE 'unknown' end) as stay_city_name_new
      ,MAX(CASE WHEN B.WORK_CITY_NAME_NEW IS NOT NULL THEN B.WORK_CITY_NAME_NEW ELSE 'unknown' end) as work_city_name_new
      ,MAX(B.STAY_WORK_DIS)  AS STAY_WORK_DIS
      ,MAX(CASE WHEN B.STAY_TOWN_FLAG   IS NOT NULL THEN B.STAY_TOWN_FLAG ELSE 'unknown' end )as  STAY_TOWN_FLAG
      ,MAX(B.REST_DAYS)   AS REST_DAYS
      ,MAX(B.WORK_DAYS)   AS WORK_DAYS
FROM TEMP_L_BHV_TR_CAR_M_TMP1   A
LEFT JOIN (SELECT USER_ID
                  ,BILL_NO
                  ,REST_DAYS
                  ,WORK_DAYS
                  ,STAY_CITY_NAME_NEW
                  ,WORK_CITY_NAME_NEW
                  ,round((2*asin(sqrt(power(sin((STAY_LATITUDE-WORK_LATITUDE)*pi()/180/2),2)+cos(STAY_LATITUDE*pi()/180)*cos(WORK_LATITUDE*pi()/180)*power(sin((STAY_LONGITUDE-WORK_LONGITUDE) *pi()/180/2),2)))*6378.137)*10000)/10000  STAY_WORK_DIS  --公里
                  ,CASE WHEN STAY_TOWN_NAME_NEW LIKE '%街道%' THEN '城镇居民' ELSE '非城镇居民' END  STAY_TOWN_FLAG
           FROM DWFU_HIVE_DB.A_TPOS_STAY_PRODUCT_D
           WHERE P_DAY = '${curmlastday}'
           )B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
GROUP BY A.USER_ID
      ,A.BILL_NO
;

--业务使用
----5.DWFU_HIVE_DB.A_UPRD_USER_BUSI_USE_M  mtaskid
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP4;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP4
AS
SELECT A.USER_ID
       ,A.BILL_NO
       ,B.TOT_CALL_CNT
       ,B.TOT_CALL_DUR
       ,ROUND(B.NET_FLUX/1024/1024,0)       AS NET_FLUX
FROM TEMP_L_BHV_TR_CAR_M_TMP1  A
LEFT JOIN (SELECT USER_ID
                  ,BILL_NO
                  ,TOT_CALL_CNT
                  ,LM_TOT_CALL_CNT
                  ,L2M_TOT_CALL_CNT
                  ,TOT_CALL_DUR
                  ,LM_TOT_CALL_DUR
                  ,L2M_TOT_CALL_DUR
                  ,NET_FLUX
                  ,LM_NET_FLUX
                  ,L2M_NET_FLUX
           FROM DWFU_HIVE_DB.A_UPRD_USER_BUSI_USE_M
           WHERE P_MON='${mtaskid}'
           )B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
;

----6.交往圈
---DWFU_HIVE_DB.I_USOC_COMM_ALL_M  mtaskid
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP5;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP5
AS
SELECT A.USER_ID
       ,A.BILL_NO
       ,B.OPP_NUMBER_CNT
FROM TEMP_L_BHV_TR_CAR_M_TMP1  A
LEFT JOIN (SELECT USER_ID
                  ,BILL_NO
                  ,COUNT(DISTINCT OPP_NUMBER)   AS OPP_NUMBER_CNT
           FROM DWFU_HIVE_DB.I_USOC_COMM_ALL_M
           WHERE P_MON='${mtaskid}'
           GROUP BY USER_ID
                  ,BILL_NO
           )B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
;

----7.消费视图
--DWFU_HIVE_DB.A_UPAY_USER_ATTR_M  mtaskid
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP6;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP6
AS
SELECT A.USER_ID
       ,A.BILL_NO
       ,B.FACT_FEE
       ,B.N3M_AVG_FACT_FEE
       ,B.CALL_FEE
       ,B.N3M_AVG_CALL_FEE
       ,B.GPRS_FEE
       ,B.N3M_AVG_GPRS_FEE
       ,B.CONSUME_LEV
FROM TEMP_L_BHV_TR_CAR_M_TMP1  A
LEFT JOIN (SELECT USER_ID
                  ,BILL_NO
                  ,FACT_FEE
                  ,L1M_FACT_FEE
                  ,L2M_FACT_FEE
                  ,N3M_AVG_FACT_FEE
                  ,CALL_FEE
                  ,L1M_CALL_FEE
                  ,L2M_CALL_FEE
                  ,N3M_AVG_CALL_FEE
                  ,GPRS_FEE
                  ,L1M_GPRS_FEE
                  ,L2M_GPRS_FEE
                  ,N3M_AVG_GPRS_FEE
                  ,CONSUME_LEV
           FROM DWFU_HIVE_DB.A_UPAY_USER_ATTR_M
           WHERE P_MON='${mtaskid}'
           )B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
;

---特殊职业,车主|司机
---DWFU_HIVE_DB.I_TNET_APP_USERS_M P_MONTH='${mtaskid}'  DEFAULT.D_CDM_APP_NAME_CODE ${curmlastday}
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP8;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP8
AS
SELECT  A.USER_ID
        ,A.BILL_NO
        ,SUM(B.PV)    AS DRV_APP_CNT
FROM TEMP_L_BHV_TR_CAR_M_TMP1 A
LEFT JOIN (SELECT BILL_NO
             ,USER_ID
             ,APP_CODE
             ,PV
      FROM DWFU_HIVE_DB.I_TNET_APP_USERS_M
      WHERE P_MONTH IN ('${mtaskid}','${lm_mtaskid}','${l2m_mtaskid}')
      ) B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
INNER JOIN (SELECT APP_NAME,APP_CODE
           FROM DEFAULT.D_CDM_APP_NAME_CODE 
           WHERE P_DAY = '${curmlastday}'
           AND  regexp_extract(APP_NAME,'车主|加油|司机|车险|交警|汽车保养|汽车维修|违章',0) <>''
           AND  regexp_extract(APP_NAME,'招募|老司机|直播|嘀嗒|平安好车主',0) =''
           GROUP BY APP_NAME,APP_CODE
           ) C
ON B.APP_CODE = C.APP_CODE
GROUP BY A.USER_ID
        ,A.BILL_NO
;

---违章、车管所
--BX_BQK_I201_SMS_M P_MON='${mtaskid}'
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP11;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP11
AS
SELECT A.USER_ID
       ,A.BILL_NO
       ,SUM(SMS_CNT)   AS WZ_SMS_CNT
FROM TEMP_L_BHV_TR_CAR_M_TMP1 A
LEFT JOIN (SELECT BILL_NO
             ,USER_ID
             ,illegal_num  AS SMS_CNT
      FROM SJWJ_HIVE_DB.L_BHV_CREDIT_TRAFFIC_ILLEGAL_M
      WHERE P_MON IN ('${mtaskid}','${l6m_mtaskid}','${taskid?calDate(-12,'M','yyyyMM')}')
      ) B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
GROUP BY A.USER_ID
        ,A.BILL_NO
;

----基站速度参数
--sjwj_hive_db.l_bhv_tr_type_lacci_d   substr(p_day,1,6)='${mtaskid}'
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP13;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP13
AS
select t1.bill_no
       ,t1.cust_name
       ,count(1) work_cnt
       ,concat(floor(avg(out_stime)/3600),':',floor(pmod(avg(out_stime),3600)/60),':',pmod(avg(out_stime),60)) out_stime_avg
       ,avg(out_stime)/60.0 out_stime_avg1
       ,avg(back_stime)/60.0 back_stime_avg1
       ,std(out_stime) out_stime_std
       ,concat(floor(avg(back_stime)/3600),':',floor(pmod(avg(back_stime),3600)/60),':',pmod(avg(back_stime),60)) back_stime_avg
       ,std(back_stime) back_stime_std
       ,avg(time_tot) time_tot_avg
       ,std(time_tot) time_tot_std
       ,avg(dis_tot ) dis_tot_avg
       ,std(dis_tot ) dis_tot_std
       ,avg(max_speed ) max_speed_avg
       ,std(max_speed) max_speed_std
       ,avg(min_speed ) min_speed_avg
       ,std(min_speed ) min_speed_std
       ,avg(speed_avg ) speed_avg_avg
       ,std(speed_avg ) speed_avg_std
       ,avg(speed_std ) speed_std_avg
       ,std(speed_std ) speed_std_std
       ,avg(flux_tot ) flux_tot_avg
       ,std(flux_tot ) flux_tot_std
       ,avg(visit_tot ) visit_tot_avg
       ,std(visit_tot ) visit_tot_std
       ,avg(map_visit_cnt ) map_visit_cnt_avg
       ,std(map_visit_cnt ) map_visit_cnt_std
       ,avg(app_cnt ) app_cnt_avg
       ,std(app_cnt ) app_cnt_std
       ,avg(lacci_cnt ) lacci_cnt_avg
       ,std(lacci_cnt ) lacci_cnt_std
       ,avg(atan_speed ) atan_speed_avg
       ,std(atan_speed ) atan_speed_std
       ,avg(atan_app ) atan_app_avg
       ,std(atan_app ) atan_app_std
       ,nvl(sum(is_subway),0)/count(1) subway_probabi
from (select hour(out_time)*3600+minute(out_time)*60+second(out_time) out_stime
            ,hour(back_time)*3600+minute(back_time)*60+second(back_time) back_stime
            ,bill_no
            ,cust_name
            ,time_tot
            ,dis_tot
            ,max_speed
            ,min_speed
            ,speed_avg
            ,speed_std
            ,flux_tot
            ,visit_tot
            ,app_cnt
            ,map_visit_cnt
            ,map_app_cnt
            ,lacci_cnt
            ,subway_cnt
            ,atan_speed
            ,atan_app
            ,is_subway
            ,out_type
       from sjwj_hive_db.l_bhv_tr_type_lacci_d 
       where p_day between '${taskid}' and REPLACE(date_sub(CURRENT_TIMESTAMP,2),'-','')
       ) t1
group by t1.bill_no,t1.cust_name
;

--异常值、缺失值处理
DROP TABLE IF EXISTS QS_L_BHV_TR_CAR_M_TMP0;
CREATE TABLE QS_L_BHV_TR_CAR_M_TMP0
(USER_ID                   STRING             COMMENT'用户编号'
,BILL_NO                   STRING             COMMENT'用户号码'
,CITY_ID                   STRING             COMMENT'归属地市'
,AGE                       INT                COMMENT'年龄'
,SEX_NEW                   STRING             COMMENT'性别'
,ORIGIN                    STRING             COMMENT'户籍'
,REAL_NAME_FLAG_NEW        STRING             COMMENT'实名认证标识'
,INNET_DUR                 INT                COMMENT'入网时长'
,VPMN_FLAG                 STRING             COMMENT'是否虚拟网成员       '
,GPR_MEMB_FLAG             STRING             COMMENT'是否集团网成员       '
,VIP_FLAG                  STRING             COMMENT'是否大客户'
,UPAY_FLAG                 STRING             COMMENT'统一支付用户标识      '
,FAMSTRU                   STRING             COMMENT'家庭结构          '
,OCCU                      STRING             COMMENT'职业            '
,SUB_OCCU_NAME             STRING             COMMENT'细分的职业         '
,LIFE_STAGE                STRING             COMMENT'人生阶段              '
,EXECUTIVE_SCORE           DECIMAL(18,2)                COMMENT'企业高管概率            '
,BUSINESS_SCORE            DECIMAL(18,2)                COMMENT'商务人士概率            '
,IF_SALARIAT               STRING             COMMENT'是否工薪阶层            '
,INCOME_LEVEL              INT                COMMENT'收入水平            '
,MIGRANT_WORKER_P          DECIMAL(18,2)                COMMENT'外来务工概率            '
,EDU_LEVEL                 STRING             COMMENT'教育程度              '
,STAY_CITY_NAME_NEW        STRING             COMMENT'居住城市              '
,WORK_CITY_NAME_NEW        STRING             COMMENT'工作城市              '
,STAY_WORK_DIS             INT                COMMENT'工作居住距离            '
,STAY_TOWN_FLAG            STRING             COMMENT'是否城镇居民            '
,TOT_CALL_CNT              INT                COMMENT'本月通话总次数           '
,OPP_NUMBER_CNT            INT                COMMENT'本月通话总个数           '
,TOT_CALL_DUR              INT                COMMENT'本月通话总时长           '
,NET_FLUX                  INT                COMMENT'移动数据上网流量(M)       '
,FACT_FEE                  INT                COMMENT'本月出账费             '
,N3M_AVG_FACT_FEE          INT                COMMENT'近三月平均出账费          '
,CALL_FEE                  INT                COMMENT'本月通话费             '
,N3M_AVG_CALL_FEE          INT                COMMENT'近三月平均通话费          '
,GPRS_FEE                  INT                COMMENT'本月数据流量费           '
,N3M_AVG_GPRS_FEE          INT                COMMENT'近三月平均数据流量费        '
,CONSUME_LEV               INT                COMMENT'消费能力标识（总体消费划分）    '
,FIR_IMEI_BRAND            STRING             COMMENT'排名第一终端品牌          '
,FIR_IMEI_PRICE            INT                COMMENT'排名第一终端价格          '
,FIR_IMEI_USE_DAYS         INT                COMMENT'排名第一终端使用天数        '
,NEW_IMEI_FLAG             STRING             COMMENT'新手机标记        '
,DRV_APP_CNT               INT                COMMENT'车主/司机版APP使用次数     '
,DRV_FLAG                  STRING             COMMENT'是否司机'   
,WZ_SMS_CNT                INT                COMMENT'近一年违章短信接收次数       '
,REST_DAYS                 INT                COMMENT'休息天数              '
,WORK_DAYS                 INT                COMMENT'工作天数              '
,WORK_CNT                  INT                COMMENT'出行次数              '
,OUT_STIME_AVG             DECIMAL(18,2)                COMMENT'外出时间均值            '
,OUT_STIME_STD             DECIMAL(18,2)                COMMENT'外出时间平方差           '
,BACK_STIME_AVG            DECIMAL(18,2)                COMMENT'返回时间均值            '
,BACK_STIME_STD            DECIMAL(18,2)                COMMENT'返回时间平方差           '
,TIME_TOT_AVG              INT                          COMMENT'平均总用时             '
,TIME_TOT_STD              DECIMAL(18,2)                COMMENT'总用时平方差            '
,DIS_TOT_AVG               DECIMAL(18,2)                COMMENT'总距离均值             '
,DIS_TOT_STD               DECIMAL(18,2)                COMMENT'总距离平方差            '
,MAX_SPEED_AVG             DECIMAL(18,2)                COMMENT'最大速度均值            '
,MAX_SPEED_STD             DECIMAL(18,2)                COMMENT'最大速度平方差           '
,MIN_SPEED_AVG             DECIMAL(18,2)                COMMENT'最小速度均值            '
,MIN_SPEED_STD             DECIMAL(18,2)                COMMENT'最小速度平方差           '
,SPEED_AVG_AVG             DECIMAL(18,2)                COMMENT'平均速度              '
,SPEED_AVG_STD             DECIMAL(18,2)                COMMENT'平均速度平方差           '
,ATAN_SPEED_AVG            DECIMAL(18,2)                COMMENT'速度参数均值            '
,ATAN_SPEED_STD            DECIMAL(18,2)                COMMENT'速度参数平方差           '
,SPEED_STD_AVG             DECIMAL(18,2)                COMMENT'速度平方差均值           '
,SPEED_STD_STD             DECIMAL(18,2)                COMMENT'速度平方差方差           '
,FLUX_TOT_AVG              DECIMAL(18,2)                COMMENT'途中总流量均值           '
,FLUX_TOT_STD              DECIMAL(18,2)                COMMENT'途中总流量平方差          '
,VISIT_TOT_AVG             DECIMAL(18,2)                COMMENT'途中总访问次数均值         '
,VISIT_TOT_STD             DECIMAL(18,2)                COMMENT'途中总访问次数平方差        '
,MAP_VISIT_CNT_AVG         DECIMAL(18,2)                COMMENT'途中地图访问次数均值        '
,MAP_VISIT_CNT_STD         DECIMAL(18,2)                COMMENT'途中地图访问次数平方差       '
,ATAN_APP_AVG              DECIMAL(18,2)                COMMENT'app参数均值           '
,ATAN_APP_STD              DECIMAL(18,2)                COMMENT'app参数平方差          '
,APP_CNT_AVG               DECIMAL(18,2)                COMMENT'途中app访问数均值        '
,APP_CNT_STD               DECIMAL(18,2)                COMMENT'途中app访问数平方差       '
,LACCI_CNT_AVG             DECIMAL(18,2)                COMMENT'途中基站数均值           '
,LACCI_CNT_STD             DECIMAL(18,2)                COMMENT'途中基站数平方差                '
)
;

INSERT OVERWRITE TABLE QS_L_BHV_TR_CAR_M_TMP0
SELECT  USER_ID
,BILL_NO
,CITY_ID
,case when age is null then 40 when age<0 then 0 when age>78 then 78 else age end as age
,SEX_NEW
,ORIGIN
,REAL_NAME_FLAG_NEW
,case when innet_dur is null then 59 when innet_dur<1 then 1 when innet_dur>242 then 242 else innet_dur end as innet_dur
,VPMN_FLAG
,GPR_MEMB_FLAG
,VIP_FLAG
,UPAY_FLAG
,FAMSTRU
,OCCU
,SUB_OCCU_NAME
,LIFE_STAGE
,case when executive_score is null then 0 when executive_score<0 then 0 else executive_score end as executive_score
,case when business_score is null then 0 when business_score<0 then 0 else business_score end as business_score
,IF_SALARIAT
,INCOME_LEVEL
,case when migrant_worker_p is null then 0 when migrant_worker_p<0 then 0 else migrant_worker_p end as migrant_worker_p
,EDU_LEVEL
,STAY_CITY_NAME_NEW
,WORK_CITY_NAME_NEW
,case when stay_work_dis is null then 0 when stay_work_dis<0 then 0 when stay_work_dis>94 then 94 else stay_work_dis end as stay_work_dis
,STAY_TOWN_FLAG
,case when tot_call_cnt is null then 71 when tot_call_cnt<0 then 0 when tot_call_cnt>1239 then 1239 else tot_call_cnt end as tot_call_cnt
,case when opp_number_cnt is null then 22 when opp_number_cnt<1 then 1 when opp_number_cnt>265 then 265 else opp_number_cnt end as opp_number_cnt
,case when tot_call_dur is null then 142 when tot_call_dur<0 then 0 when tot_call_dur>2371 then 2371 else tot_call_dur end as tot_call_dur
,case when net_flux is null then 873 when net_flux<0 then 0 when net_flux>61040.6 then 61040.6 else net_flux end as net_flux
,case when fact_fee is null then 5800 when fact_fee<0 then 0 when fact_fee>32041 then 32041 else fact_fee end as fact_fee
,case when n3m_avg_fact_fee is null then 5800 when n3m_avg_fact_fee<0 then 0 when n3m_avg_fact_fee>30192 then 30192 else n3m_avg_fact_fee end as n3m_avg_fact_fee
,case when call_fee is null then 500 when call_fee<0 then 0 when call_fee>11507 then 11507 else call_fee end as call_fee
,case when n3m_avg_call_fee is null then 500 when n3m_avg_call_fee<0 then 0 when n3m_avg_call_fee>9253 then 9253 else n3m_avg_call_fee end as n3m_avg_call_fee
,case when gprs_fee is null then 3000 when gprs_fee<0 then 0 when gprs_fee>16000 then 16000 else gprs_fee end as gprs_fee
,case when n3m_avg_gprs_fee is null then 3000 when n3m_avg_gprs_fee<0 then 0 when n3m_avg_gprs_fee>16000 then 16000 else n3m_avg_gprs_fee end as n3m_avg_gprs_fee
,CONSUME_LEV
,FIR_IMEI_BRAND
,case when fir_imei_price is null then 1800 when fir_imei_price<-99 then -99 when fir_imei_price>8580 then 8580 else fir_imei_price end as fir_imei_price
,case when fir_imei_use_days is null then 333 when fir_imei_use_days<3 then 3 when fir_imei_use_days>1468 then 1468 else fir_imei_use_days end as fir_imei_use_days
,NEW_IMEI_FLAG
,case when drv_app_cnt is null then 0 when drv_app_cnt<0 then 0 when drv_app_cnt>40 then 40 else drv_app_cnt end as drv_app_cnt
,CASE WHEN drv_app_cnt > 0 THEN '司机' ELSE '非司机' end as drv_flag
,case when wz_sms_cnt is null then 0 when wz_sms_cnt<0 then 0 when wz_sms_cnt>57 then 57 else wz_sms_cnt end as wz_sms_cnt
,case when rest_days is null then 14 when rest_days<0 then 0 when rest_days>30 then 30 else rest_days end as rest_days
,case when work_days is null then 14 when work_days<0 then 0 when work_days>20 then 20 else work_days end as work_days
,case when work_cnt is null then 0 when work_cnt<0 then 0 when work_cnt>24 then 24 else work_cnt end as work_cnt
,case when out_stime_avg is null then -99 when out_stime_avg<-99 then -99 when out_stime_avg>1074.73 then 1074.73 else out_stime_avg end as out_stime_avg
,case when out_stime_std is null then -99 when out_stime_std<-99 then -99 when out_stime_std>17768.68 then 17768.68 else out_stime_std end as out_stime_std
,case when back_stime_avg is null then -99 when back_stime_avg<-99 then -99 when back_stime_avg>1136.77 then 1136.77 else back_stime_avg end as back_stime_avg
,case when back_stime_std is null then -99 when back_stime_std<-99 then -99 when back_stime_std>18114.39 then 18114.39 else back_stime_std end as back_stime_std
,case when time_tot_avg is null then -99 when time_tot_avg<-99 then -99 when time_tot_avg>137 then 137 else time_tot_avg end as time_tot_avg
,case when time_tot_std is null then -99 when time_tot_std<-99 then -99 when time_tot_std>54.18 then 54.18 else time_tot_std end as time_tot_std
,case when dis_tot_avg is null then -99 when dis_tot_avg<-99 then -99 when dis_tot_avg>41340.08 then 41340.08 else dis_tot_avg end as dis_tot_avg
,case when dis_tot_std is null then -99 when dis_tot_std<-99 then -99 when dis_tot_std>16480.93 then 16480.93 else dis_tot_std end as dis_tot_std
,case when max_speed_avg is null then -99 when max_speed_avg<-99 then -99 when max_speed_avg>852.66 then 852.66 else max_speed_avg end as max_speed_avg
,case when max_speed_std is null then -99 when max_speed_std<-99 then -99 when max_speed_std>1546.39 then 1546.39 else max_speed_std end as max_speed_std
,case when min_speed_avg is null then -99 when min_speed_avg<-99 then -99 when min_speed_avg>19.07 then 19.07 else min_speed_avg end as min_speed_avg
,case when min_speed_std is null then -99 when min_speed_std<-99 then -99 when min_speed_std>12.35 then 12.35 else min_speed_std end as min_speed_std
,case when speed_avg_avg is null then -99 when speed_avg_avg<-99 then -99 when speed_avg_avg>41.5 then 41.5 else speed_avg_avg end as speed_avg_avg
,case when speed_avg_std is null then -99 when speed_avg_std<-99 then -99 when speed_avg_std>16.97 then 16.97 else speed_avg_std end as speed_avg_std
,case when atan_speed_avg is null then -99 when atan_speed_avg<-99 then -99 when atan_speed_avg>0.91 then 0.91 else atan_speed_avg end as atan_speed_avg
,case when atan_speed_std is null then -99 when atan_speed_std<-99 then -99 when atan_speed_std>0.24 then 0.24 else atan_speed_std end as atan_speed_std
,case when speed_std_avg is null then -99 when speed_std_avg<-99 then -99 when speed_std_avg>306.16 then 306.16 else speed_std_avg end as speed_std_avg
,case when speed_std_std is null then -99 when speed_std_std<-99 then -99 when speed_std_std>567.98 then 567.98 else speed_std_std end as speed_std_std
,case when flux_tot_avg is null then -99 when flux_tot_avg<-99 then -99 when flux_tot_avg>23216949.96 then 23216949.96 else flux_tot_avg end as flux_tot_avg
,case when flux_tot_std is null then -99 when flux_tot_std<-99 then -99 when flux_tot_std>27953625.96 then 27953625.96 else flux_tot_std end as flux_tot_std
,case when visit_tot_avg is null then -99 when visit_tot_avg<-99 then -99 when visit_tot_avg>305.06 then 305.06 else visit_tot_avg end as visit_tot_avg
,case when visit_tot_std is null then -99 when visit_tot_std<-99 then -99 when visit_tot_std>202.4 then 202.4 else visit_tot_std end as visit_tot_std
,case when map_visit_cnt_avg is null then -99 when map_visit_cnt_avg<-99 then -99 when map_visit_cnt_avg>0 then 0 else map_visit_cnt_avg end as map_visit_cnt_avg
,case when map_visit_cnt_std is null then -99 when map_visit_cnt_std<-99 then -99 when map_visit_cnt_std>0 then 0 else map_visit_cnt_std end as map_visit_cnt_std
,case when atan_app_avg is null then -99 when atan_app_avg<-99 then -99 when atan_app_avg>0.98 then 0.98 else atan_app_avg end as atan_app_avg
,case when atan_app_std is null then -99 when atan_app_std<-99 then -99 when atan_app_std>0.38 then 0.38 else atan_app_std end as atan_app_std
,case when app_cnt_avg is null then -99 when app_cnt_avg<-99 then -99 when app_cnt_avg>7 then 7 else app_cnt_avg end as app_cnt_avg
,case when app_cnt_std is null then -99 when app_cnt_std<-99 then -99 when app_cnt_std>2.68 then 2.68 else app_cnt_std end as app_cnt_std
,case when lacci_cnt_avg is null then -99 when lacci_cnt_avg<-99 then -99 when lacci_cnt_avg>90.14 then 90.14 else lacci_cnt_avg end as lacci_cnt_avg
,case when lacci_cnt_std is null then -99 when lacci_cnt_std<-99 then -99 when lacci_cnt_std>49.83 then 49.83 else lacci_cnt_std end as lacci_cnt_std
FROM L_BHV_TR_CAR_M_TMP0
;

-- 建表
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_predict_result;
create table if not exists TEMP_L_BHV_TR_CAR_M_predict_result
(
bill_no  STRING
,p_value STRING -- ==> 预测值
,flag  STRING
)
;

-- 变量赋值
V_CITY_ID=['570','571','572','573','574','575','576','577','578','579','580'];

select * from qs_l_bhv_tr_car_m_tmp0  WHERE CITY_ID='${V_CITY_ID[i]}'

-- 往预测结果表中插入数据
insert into TEMP_L_BHV_TR_CAR_M_predict_result
select 
bill_no
,p_value
,flag
from TEMP_L_BHV_TR_CAR_M_${V_CITY_ID[i]}
;

---打车一族
--DWFU_HIVE_DB.I_TNET_APP_USERS_M  P_MONTH='${mtaskid}'
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_TMP10;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_TMP10
AS
SELECT A.USER_ID
       ,A.BILL_NO
       ,SUM(B.PV)    AS TAXI_APP_CNT
FROM TEMP_L_BHV_TR_CAR_M_TMP1 A
LEFT JOIN (SELECT BILL_NO
             ,USER_ID
             ,APP_CODE
             ,PV
      FROM DWFU_HIVE_DB.I_TNET_APP_USERS_M
      WHERE P_MONTH IN ('${mtaskid}','${lm_mtaskid}','${l2m_mtaskid}')
      ) B
ON A.USER_ID = B.USER_ID
AND A.BILL_NO = B.BILL_NO
INNER JOIN (SELECT APP_NAME,APP_CODE
            FROM DEFAULT.D_CDM_APP_NAME_CODE 
            WHERE P_DAY = '${curmlastday}'
            AND  regexp_extract(APP_NAME,'出行|专车|滴滴|嘀嗒|首约|约车|打车|顺风车|用车',0) <>''
            AND  regexp_extract(APP_NAME,'司机|加油|车主|企业',0) =''
            GROUP BY APP_NAME,APP_CODE
           ) C
ON B.APP_CODE = C.APP_CODE
GROUP BY A.USER_ID
        ,A.BILL_NO
;

--规则调整
DROP TABLE IF EXISTS TEMP_L_BHV_TR_CAR_M_predict_result_TMP21;
CREATE TABLE TEMP_L_BHV_TR_CAR_M_predict_result_TMP21
AS
SELECT B.USER_ID
       ,A.BILL_NO
       ,B.CITY_ID
       ,CASE WHEN B.WZ_SMS_CNT >= 1  THEN 1
             WHEN B.AGE <= 25 AND D.USER_ID IS NOT NULL AND A.P_VALUE < 0.5 THEN A.P_VALUE 
             WHEN B.AGE <= 25 AND D.USER_ID IS NOT NULL AND A.P_VALUE >= 0.5 THEN A.P_VALUE-0.5
             WHEN B.DRV_APP_CNT >= 15 AND A.P_VALUE > 0.7 THEN A.P_VALUE
             WHEN B.DRV_APP_CNT >= 5 AND A.P_VALUE <= 0.7  THEN CASE WHEN A.P_VALUE+B.DRV_APP_CNT/90*0.5 >= 1 THEN 1
                                                                  ELSE A.P_VALUE+B.DRV_APP_CNT/90*0.5 END
             WHEN C.TAXI_APP_CNT >= 1 AND A.P_VALUE < 0.5 THEN A.P_VALUE
             WHEN C.TAXI_APP_CNT >= 5 AND A.P_VALUE >= 0.5  THEN CASE WHEN A.P_VALUE-TAXI_APP_CNT/90*0.5 <= 0 THEN 0
                                                                  ELSE A.P_VALUE-TAXI_APP_CNT/90*0.5 END
             ELSE A.P_VALUE END AS P_VALUE
FROM TEMP_L_BHV_TR_CAR_M_predict_result A
INNER JOIN (
SELECT USER_ID 
,BILL_NO
,CITY_ID
,AGE
,wz_sms_cnt
,DRV_APP_CNT
FROM QS_L_BHV_TR_CAR_M_TMP0
)B
ON A.BILL_NO = B.BILL_NO
LEFT JOIN TEMP_L_BHV_TR_CAR_M_TMP10 C
ON A.BILL_NO = C.BILL_NO
LEFT JOIN (SELECT USER_ID,BILL_ID
          FROM DEFAULT.D_BBI_ZZQS_USER_VPMN
          WHERE P_DAY = REPLACE(date_sub(CURRENT_TIMESTAMP,2),'-','')
          AND (VPMN_NAME like '%学院%'
           OR VPMN_NAME like '%大学%'
           OR VPMN_NAME like '%学校%'
           OR GROUP_NAME LIKE '%学生集团%')
          AND SUBSTR(VPMN_JOIN_DATE,1,4) >= ${l2y_ytaskid}
          GROUP BY USER_ID,BILL_ID
          )D
ON B.USER_ID = D.USER_ID

--has_car
drop table if exists zqs_ryj_has_car;
create table zqs_ryj_has_car as
select  ta.bill_no
        ,ta.user_id
        ,ta.city_id
        ,ta.age
        ,ta.sex
        ,ta.cust_name
        ,ta.card_type
        ,ta.card_code
        ,ta.work_lacci_name
        ,ta.stay_lacci_name
        ,ta.work_stay_distance
        ,ta.rest_days
        ,ta.work_days
        ,t1.out_stime_avg
        ,t1.back_stime_avg
        ,t1.time_tot_avg
        ,t1.dis_tot_avg
        ,t1.speed_avg_avg
        ,t1.flux_tot_avg
        ,t1.app_cnt_avg
        ,t1.lacci_cnt_avg
        ,t2.call_cnt_tot call_cnt
        ,t3.app_cnt
        ,t3.flux_mb
from tmp_ryj_has_car_basic_user ta
left join tmp_ryj_tr_type_lacci_tot t1 on ta.bill_no=t1.bill_no
left join tmp_ryj_has_car_call t2 on ta.bill_no=t2.bill_no
left join tmp_ryj_has_car_app t3 on ta.bill_no=t3.bill_no
;

--有车一族结果表
insert overwrite table L_BHV_TR_CAR_M
partition(P_MON='${mtaskid}')
select tt.bill_no
       ,tt.user_id
       ,tt.city_id
       ,tt.age
       ,tt.sex
       ,tt.cust_name
       ,tt.card_type
       ,tt.card_code
       ,nvl(t1.work_lacci_name ,t2.work_lacci_name )
       ,nvl(t1.stay_lacci_name ,t2.stay_lacci_name )
       ,nvl(t1.work_stay_distance ,t2.work_stay_distance )
       ,nvl(t1.rest_days ,t2.rest_days )
       ,nvl(t1.work_days ,t2.work_days )
       ,nvl(t1.out_stime_avg ,t2.out_stime_avg )
       ,nvl(t1.back_stime_avg ,t2.back_stime_avg )
       ,nvl(t1.time_tot_avg ,t2.time_tot_avg )
       ,nvl(t1.dis_tot_avg ,t2.dis_tot_avg )
       ,nvl(t1.speed_avg_avg ,t2.speed_avg_avg )
       ,nvl(t1.flux_tot_avg ,t2.flux_tot_avg )
       ,nvl(t1.app_cnt_avg ,t2.app_cnt_avg )
       ,nvl(t1.lacci_cnt_avg ,t2.lacci_cnt_avg )
       ,nvl(t1.call_cnt ,t2.call_cnt )
       ,nvl(t1.app_cnt ,t2.app_cnt )
       ,nvl(t1.flux_mb ,t2.flux_mb )
       ,case when t3.P_VALUE >= 0.6 then 1 else 0 end has_car
       ,t3.P_VALUE    AS car_probabi
from  TEMP_L_BHV_TR_CAR_M_TMP1 tt
left join (SELECT USER_ID
      ,BILL_NO
      ,MAX(work_lacci_name)             AS work_lacci_name
      ,MAX(stay_lacci_name     )        AS stay_lacci_name
      ,MAX(work_stay_distance  )        AS work_stay_distance
      ,MAX(rest_days           )        AS rest_days
      ,MAX(work_days           )        AS work_days
      ,MAX(out_stime_avg       )        AS out_stime_avg
      ,MAX(back_stime_avg      )        AS back_stime_avg
      ,MAX(time_tot_avg        )        AS time_tot_avg
      ,MAX(dis_tot_avg         )        AS dis_tot_avg
      ,MAX(speed_avg_avg       )        AS speed_avg_avg
      ,MAX(flux_tot_avg        )        AS flux_tot_avg
      ,MAX(app_cnt_avg         )        AS app_cnt_avg
      ,MAX(lacci_cnt_avg       )        AS lacci_cnt_avg
      ,MAX(call_cnt            )        AS call_cnt
      ,MAX(app_cnt             )        AS app_cnt
      ,MAX(flux_mb             )        AS flux_mb
            FROM zqs_ryj_has_car 
            GROUP BY USER_ID
                  ,BILL_NO
            )t1 
on tt.bill_no=t1.bill_no
AND TT.USER_ID = T1.USER_ID
LEFT JOIN TEMP_L_BHV_TR_CAR_M_predict_result_TMP21 T3
on tt.bill_no=t3.bill_no
AND TT.USER_ID = T3.USER_ID
left join (SELECT USER_ID
      ,BILL_NO
      ,MAX(work_lacci_name)             AS work_lacci_name
      ,MAX(stay_lacci_name     )        AS stay_lacci_name
      ,MAX(work_stay_distance  )        AS work_stay_distance
      ,MAX(rest_days           )        AS rest_days
      ,MAX(work_days           )        AS work_days
      ,MAX(out_stime_avg       )        AS out_stime_avg
      ,MAX(back_stime_avg      )        AS back_stime_avg
      ,MAX(time_tot_avg        )        AS time_tot_avg
      ,MAX(dis_tot_avg         )        AS dis_tot_avg
      ,MAX(speed_avg_avg       )        AS speed_avg_avg
      ,MAX(flux_tot_avg        )        AS flux_tot_avg
      ,MAX(app_cnt_avg         )        AS app_cnt_avg
      ,MAX(lacci_cnt_avg       )        AS lacci_cnt_avg
      ,MAX(call_cnt            )        AS call_cnt
      ,MAX(app_cnt             )        AS app_cnt
      ,MAX(flux_mb             )        AS flux_mb
            FROM sjwj_hive_db.L_BHV_TR_CAR_M t2 
            where t2.p_mon='${lm_mtaskid}'
            GROUP BY USER_ID
                  ,BILL_NO
            ) t2
on tt.bill_no = t2.bill_no
and tt.user_id = t2.user_id
;