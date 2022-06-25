-- 获取工作或者居住在杭州的人，并且关联社会属性
drop table temp_fyuser_count_1_1;
create table temp_fyuser_count_1_1 as 
select a.*,b.sex,b.age,b.age_level,b.sex_desc,b.origin,b.imei,b.cert_type,b.cert_code
from (
select p_mon as months,bill_no,home_city_name,home_county_name,home_lng_cent,home_lat_cent,home_grid_id,home_days,work_city_name,work_county_name,work_lng_cent,work_lat_cent,work_grid_id,work_days
from dwfu_hive_db.i_tpos_address_grid_m
where length(bill_no)=11 
and substr(bill_no,1,1)=1 
and bill_no regexp '1[0-9]{10}'
and p_mon in ('202204','202205')
and ( home_city_name = '杭州市'  or  work_city_name = '杭州市' )
) a
left join (select bill_no,sex_new as sex,case when sex_new = 1 then 'M' when sex_new = 0 then 'F'  else 'N' end sex_desc,age,
case when age >= 0 and age <= 19 then '0-19'
when age >= 20 and age <= 24 then '20-24'
when age >= 25 and age <= 29 then '25-29'
when age >= 30 and age <= 34 then '30-34'
when age >= 35 and age <= 39 then '35-39'
when age >= 40 and age <= 44 then '40-44'
when age >= 45 and age <= 49 then '45-49'
when age >= 50 and age <= 54 then '50-54'
when age >= 55 and age <= 59 then '55-59'
when age >= 60 and age <= 999 then '60-999'
else 'N-N' end age_level,origin,imei,cert_type,cert_code from dwfu_hive_db.a_usoc_user_attr_m where p_mon = '202205') b on a.bill_no = b.bill_no;

-- 使用250米栅格
create table temp_fyuser_count_250_6_20 as
select b.SEC_MR_CENT_ID, b.SEC_MR_LAT_CENT, b.SEC_MR_LNG_CENT, a.bill_no, a.months, a.age_level, a.sex_desc, a.cert_type, a.cert_code, a.home_county_name, a.work_county_name, a.home_city_name, a.work_city_name
from temp_fyuser_count_1_1 a
join dwfu_hive_db.I_CDM_SEC_MR_RELA b
on a.home_grid_id = b.id

-- 1.1.1
create table temp_fyuser_count_250_6_20_1_1 as
select SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20
where home_county_name = '富阳区' and cert_type = 1 and substr(cert_code,1,6) in ('330183','330123')
group by SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, months
order by cnt desc;

select age_level,sex_desc,count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20
where home_county_name = '富阳区'  and cert_type = 1 and substr(cert_code,1,6) in ('330183','330123')
group by age_level,sex_desc,months;

-- 1.1.2
create table temp_fyuser_count_250_6_20_1_2 as
select SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20
where home_county_name = '富阳区' and cert_type = 1 and substr(cert_code,1,6) not in ('330183','330123')
group by SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, months
order by cnt desc;

select age_level,sex_desc,count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20 
where home_county_name = '富阳区'  and cert_type = 1 and substr(cert_code,1,6) not in ('330183','330123')
group by age_level,sex_desc,months;

-- 1.2.1
create table temp_fyuser_count_250_6_20_1_3 as
select SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20
where home_county_name = '富阳区' and work_county_name != '富阳区'
group by SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, months
order by cnt desc;

select age_level,sex_desc,count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20 
where home_county_name = '富阳区' and work_county_name != '富阳区'
group by age_level,sex_desc,months;

-- 1.2.2
create table temp_fyuser_count_250_6_20_1_4 as
select SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20
where home_county_name = '富阳区' and work_county_name = '富阳区'
group by SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT, months
order by cnt desc;

select age_level,sex_desc,count(distinct bill_no) cnt,months 
from temp_fyuser_count_250_6_20 
where home_county_name = '富阳区' and work_county_name = '富阳区'
group by age_level,sex_desc,months;

-- 1.2.3
drop table temp_45jiejiari_user_d;
create table temp_45jiejiari_user_d as 
select a.bill_no,a.grid_id,a.grid_lng_cent,a.grid_lat_cent,substr(a.in_time,1,10) in_time_day,substr(a.in_time,1,7) in_time_months,sum(stay_duration) stay_duration
from dwfu_hive_db.i_tpos_trail_grid_d a join (select id grid_id from dwfu_hive_db.i_cdm_grid2community where p_day = '20220616' and city_name = '杭州市' and county_name = '富阳区' group by id) b on a.grid_id = b.grid_id
where a.p_day in (20220403,20220404,20220405,20220409,20220410,20220416,20220417,20220423,20220430,20220501,20220502,20220503,20220504,20220508,20220514,20220515,20220521,20220522,20220528,20220529)
and length(a.bill_no)=11 
and substr(a.bill_no,1,1)=1 
and a.bill_no regexp '1[0-9]{10}'
group by a.bill_no,a.grid_id,a.grid_lng_cent,a.grid_lat_cent,substr(a.in_time,1,10),substr(a.in_time,1,7)
;

drop table temp_fyuser_count_1_2;
create table temp_fyuser_count_1_2 as 
select * from (
select in_time_months,bill_no,grid_id,grid_lng_cent,grid_lat_cent,row_number() over(partition by in_time_months,bill_no,grid_id order by stay_duration) rn,age,age_level,sex,sex_desc
from (
select a.bill_no,a.grid_id,a.grid_lng_cent,a.grid_lat_cent,sum(a.stay_duration) as stay_duration,substr(a.in_time_day,1,7) as in_time_months,b.age,b.age_level,b.sex,b.sex_desc
from temp_45jiejiari_user_d a join (select bill_no,age,age_level,sex,sex_desc from temp_fyuser_count_1_1 where home_county_name != '富阳区' and work_county_name != '富阳区' group by bill_no,age,age_level,sex,sex_desc) b on a.bill_no = b.bill_no 
group by a.bill_no,a.grid_id,a.grid_lng_cent,a.grid_lat_cent,substr(a.in_time_day,1,7)
having sum(a.stay_duration) > 12*3600
) tmp1
) tmp2 where rn = 1
;

create table temp_fyuser_count_250_6_20_2 as
select b.SEC_MR_CENT_ID, b.SEC_MR_LAT_CENT, b.SEC_MR_LNG_CENT, a.bill_no, a.in_time_months, a.age_level, a.sex_desc
from temp_fyuser_count_1_2 a
join dwfu_hive_db.I_CDM_SEC_MR_RELA b
on a.grid_id = b.id

create table temp_fyuser_count_250_6_20_1_5 as
select SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT,count(distinct bill_no) cnt,in_time_months from temp_fyuser_count_250_6_20_2 group by SEC_MR_CENT_ID, SEC_MR_LNG_CENT, SEC_MR_LAT_CENT,in_time_months order by cnt desc;

select age_level,sex_desc,count(distinct bill_no) cnt,in_time_months from temp_fyuser_count_250_6_20_2 group by sex_desc,age_level,in_time_months;

-- 1.3
create table temp_fuyang_grid_id_college (
grid_name string,
grid_id string
)row format delimited fields terminated by ',' stored as orcfile;

-- 1.3
create table temp_fyuser_count_250_6_20_1_6_add as
select a.*, b.grid_name
from (
    select p_mon as months,bill_no,home_city_name,home_county_name,home_lng_cent,home_lat_cent,home_grid_id,home_days,work_city_name,work_county_name,work_lng_cent,work_lat_cent,work_grid_id,work_days
    from dwfu_hive_db.i_tpos_address_grid_m  
    where length(bill_no)=11 and substr(bill_no,1,1)=1 and bill_no regexp '1[0-9]{10}' and p_mon in ('202204','202205')
) a
join
(
    select * from temp_fuyang_grid_id_college
) b
on a.home_grid_id = b.grid_id or a.work_grid_id = b.grid_id

create table temp_fyuser_count_250_6_20_1_7_add as
select a.grid_name,b.term_mdl, b.imei, a.bill_no,a.months from  temp_fyuser_count_250_6_20_1_6_add a 
join (select bill_no,term_mdl, imei from dwfu_hive_db.a_usoc_user_attr_m where p_mon = '202205' and age >=18 and age <= 25) b on a.bill_no = b.bill_no

select a.grid_name, b.tele_fac, count(distinct a.bill_no), a.months
from temp_fyuser_count_250_6_20_1_7_add a
left join
(
    select imei, tele_fac from dwfu_hive_db.i_term_res_d where p_day = '20220620'
) b
on  substr(a.imei,1,8) = b.imei
group by a.grid_name, b.tele_fac, a.months

-- select grid_name, term_mdl, count(distinct bill_no), months
-- from temp_fyuser_count_250_6_20_1_7_add
-- group by grid_name, term_mdl, months

-- 1.4 到达富阳的商旅客

-- -- 富阳的所有栅格
create table temp_every_fuyang_grid as
select id, lng_join, lat_join from dwfu_hive_db.i_cdm_grid2community where p_day = '20220621' and city_name = '杭州市' and county_name = '富阳区'

-- -- 先求2021年12月到达过富阳的人
create table temp_fuyang_grid_id_visit (
grid_name string,
grid_id string
)row format delimited fields terminated by ',' stored as orcfile;

drop table temp_fyuser_count_622_202112;
create table temp_fyuser_count_622_202112 as
select a.bill_no, a.grid_id, a.grid_join, a.in_time, a.out_time, a.stay_duration, a.p_day
from dwfu_hive_db.I_TPOS_TRAIL_GRID_D a 
join temp_every_fuyang_grid b
on a.grid_id = b.id
where a.p_day >= 20211201 and a.p_day < 20220101
and length(a.bill_no)=11 
and substr(a.bill_no,1,1)=1 
and a.bill_no regexp '1[0-9]{10}';

create table temp_fyuser_count_622_202112_local as
select p_mon as months,bill_no,home_city_name,home_county_name,home_lng_cent,home_lat_cent,home_grid_id,home_days,work_city_name,work_county_name,work_lng_cent,work_lat_cent,work_grid_id,work_days
from dwfu_hive_db.i_tpos_address_grid_m  
where length(bill_no)=11 
and substr(bill_no,1,1)=1 
and bill_no regexp '1[0-9]{10}'
and p_mon = '202112'
and ( (home_city_name = '杭州市' and home_county_name = '富阳区')  or (work_city_name = '杭州市' and work_county_name = '富阳区') )

create table temp_fyuser_count_622_202112_visit as
select a.* from temp_fyuser_count_622_202112 a
left join temp_fyuser_count_622_202112_local b
on a.bill_no = b.bill_no
where b.bill_no is null

-- 全富阳游客
create table temp_fyuser_count_622_202112_visit_different_12_location_site as
select a.*, case when b.age_level is null then 'N-N' else b.age_level end age_level, case when b.sex_desc is null then 'N' else b.sex_desc end sex_desc, c.grid_name
from temp_fyuser_count_622_202112_visit a
left join (
    select bill_no,sex_new as sex,case when sex_new = 1 then 'M' when sex_new = 0 then 'F'  else 'N' end sex_desc,age,
    case when age >= 0 and age <= 19 then '0-19'
    when age >= 20 and age <= 24 then '20-24'
    when age >= 25 and age <= 29 then '25-29'
    when age >= 30 and age <= 34 then '30-34'
    when age >= 35 and age <= 39 then '35-39'
    when age >= 40 and age <= 44 then '40-44'
    when age >= 45 and age <= 49 then '45-49'
    when age >= 50 and age <= 54 then '50-54'
    when age >= 55 and age <= 59 then '55-59'
    when age >= 60 and age <= 999 then '60-999'
    else 'N-N' end age_level,origin,imei,cert_type,cert_code from dwfu_hive_db.a_usoc_user_attr_m where p_mon = '202112'
) b
on a.bill_no = b.bill_no
left join temp_fuyang_grid_id_visit c
on a.grid_id = c.grid_id

-- 任意
select a.sex_desc, a.age_level, count(distinct a.bill_no), count(a.bill_no), substr(a.p_day, 1, 6) as months
from (
  select distinct bill_no, grid_name, age_level, sex_desc, p_day from temp_fyuser_count_622_202112_visit_different_12_location_site
  where stay_duration > 1800
) a
group by a.sex_desc, a.age_level, substr(a.p_day, 1, 6)

select a.grid_name ,a.sex_desc, a.age_level, count(distinct a.bill_no), count(a.bill_no), substr(a.p_day, 1, 6) as months
from (
  select distinct bill_no, grid_name, age_level, sex_desc, p_day from temp_fyuser_count_622_202112_visit_different_12_location_site
) a
where a.grid_name is not null
group by a.grid_name, a.sex_desc, a.age_level, substr(a.p_day, 1, 6)

-- 夜晚
select a.sex_desc, a.age_level, count(distinct a.bill_no), count(a.bill_no), substr(a.p_day, 1, 6) as months
from (
  select distinct bill_no, grid_name, age_level, sex_desc, p_day from temp_fyuser_count_622_202112_visit_different_12_location_site
  where (substr(in_time, 12, 2) <= 4 and stay_duration >= 14400) or (substr(out_time, 12, 2) <= 10 and stay_duration >= 14400)
) a
group by a.sex_desc, a.age_level, substr(a.p_day, 1, 6)

select a.grid_name, a.sex_desc, a.age_level, count(distinct a.bill_no), count(a.bill_no), substr(a.p_day, 1, 6) as months
from (
  select distinct bill_no, grid_name, age_level, sex_desc, p_day from temp_fyuser_count_622_202112_visit_different_12_location_site
  where (substr(in_time, 12, 2) <= 4 and stay_duration >= 14400) or (substr(out_time, 12, 2) <= 10 and stay_duration >= 14400)
) a
where a.grid_name is not null
group by a.grid_name, a.sex_desc, a.age_level, substr(a.p_day, 1, 6)