create table temp_szh_jili_use_app_12 as
select BILL_NO, if(sum(mon_is_get_4s)>0,1,0) mon_is_get_4s, mon_day_cnt, mon_cnt1, sum(mon_cnt2) mon_cnt2, mon_is_get_city
from(
    select BILL_NO, mon_is_get_4s, count(distinct P_DAY) over(partition by BILL_NO) mon_day_cnt, count(distinct poi_name) over(partition by BILL_NO) mon_cnt1, count(distinct poi_name) over(partition by BILL_NO,P_DAY) mon_cnt2, sum(mon_is_get_city)over (partition by BILL_NO) mon_is_get_city, P_DAY
    from 
    (
        select a.BILL_NO, if(b.brand is null,0,1) mon_is_get_4s, if(a.HOME_CITY_ID<>b.p_city and a.WORK_CITY_ID<>b.p_city,1,0) mon_is_get_city, b.brand, b.poi_name, b.grid_id, b.P_DAY, b.p_city
        from temp_szh_jili_use_app_4 a
        left join temp_szh_jili_use_app_11 b
        on a.BILL_NO = b.bill_no
    )
)
group by BILL_NO, mon_day_cnt, mon_cnt1, mon_is_get_city