-- 获取居住或者工作在杭州的人
create table temp_work_home_hangzhou_0704 as
select p_mon as months,bill_no,home_city_name,home_county_name,home_lng_cent,home_lat_cent,home_grid_id,home_days,work_city_name,work_county_name,work_lng_cent,work_lat_cent,work_grid_id,work_days
from dwfu_hive_db.i_tpos_address_grid_m
where length(bill_no)=11 
and substr(bill_no,1,1)=1 
and bill_no regexp '1[0-9]{10}'
and p_mon = '202205'
and ( home_city_name = '杭州市'  or  work_city_name = '杭州市' )

---- 富阳金茂周边板块的工作常驻人口、居住常驻人口、工作和居住去重的常驻人口

-- 获取工作常驻人口
create table temp_work_home_hangzhou_0704_02_1 as
select a.*, b.location
from temp_work_home_hangzhou_0704 a
join (select * from temp_binjiang_grid_20220701 where location <> 4) b
on a.work_grid_id = b.id

-- 获取居住常驻人口
create table temp_work_home_hangzhou_0704_02_2 as
select a.*, b.location
from temp_work_home_hangzhou_0704 a
join (select * from temp_binjiang_grid_20220701 where location <> 4) b
on a.home_grid_id = b.id

-- 获取工作和居住去重的常驻人口
create table temp_work_home_hangzhou_0704_02_5 as
select a.*, b.location
from temp_work_home_hangzhou_0704 a
join (select * from temp_binjiang_grid_20220701 where location <> 4) b
on a.work_grid_id = b.id
where a.home_grid_id = b.id 


select a.site, b.sex_desc, b.age_level, count(distinct a.bill_no) from
(select
    case when location = 1 then '银湖科技城'
    when location = 2 then '高教园'
    when location = 3 then '鹿山'
    when location = 5 then '秦望广场'
    when location = 6 then '富春'
    when location = 7 then '江南'
    when location = 8 then '高桥'
    when location = 9 then '阳陂湖'
    when location = 10 then '金桥工业园'
    when location = 11 then '高尔夫路'
    when location = 12 then '东洲岛'
    when location = 13 then '滨江'
    when location = 14 then '转塘'
    end site,
 	bill_no
from temp_work_home_hangzhou_0704_02_1
where work_days >= 15) a
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
else 'N-N' end age_level,origin,imei,cert_type,cert_code from dwfu_hive_db.a_usoc_user_attr_m where p_mon = '202205') b
on a.bill_no = b.bill_no
group by a.site, b.sex_desc, b.age_level