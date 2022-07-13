-- 栅格数据
    -- 获取胡老师和张帆20220704的栅格数据
    create table temp_two_hzcompare as
    select * from dwfu_hive_db.I_TPOS_TRAIL_GRID_D where p_day = '20220704'  and bill_no in ('19558107600', '13819145656')

    -- // TODO two days
    create table temp_two_hzcompare_two as
    select * from dwfu_hive_db.I_TPOS_TRAIL_GRID_D where p_day in ('20220707', '20220708') and bill_no in ('19558107600', '13819145656')

    -- // TODO three days
    create table temp_two_hzcompare_three as
    select * from dwfu_hive_db.I_TPOS_TRAIL_GRID_D where p_day in ('20220706', '20220707', '20220708') and bill_no in ('19558107600', '13819145656')

    -- ==> 转换为二级栅格
    create table temp_two_hzcompare_sec as
    select b.SEC_MR_CENT_ID, a.*
    from temp_two_hzcompare a
    join dwfu_hive_db.I_CDM_SEC_MR_RELA b
    on a.gri_id = b.id
d
    -- // TODO two days
    create table temp_two_hzcompare_sec_two as
    select b.SEC_MR_CENT_ID, a.*
    from temp_two_hzcompare_two a
    join dwfu_hive_db.I_CDM_SEC_MR_RELA b
    on a.grid_id = b.id

    -- 获取两个人栅格相同的数据进行比较
    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.grid_id, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from
    (select * from temp_two_hzcompare where bill_no = '19558107600') a
    join
    (select * from temp_two_hzcompare where bill_no = '13819145656') b
    on a.grid_id = b.grid_id
    where (a.in_time <= b.in_time and a.out_time => b.in_time) or (b.in_time <= a.in_time and b.out_time => a.in_time)

    -- // TODO two days
    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.SEC_MR_CENT_ID, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from
    (select * from temp_two_hzcompare_sec_two where bill_no = '19558107600') a
    join
    (select * from temp_two_hzcompare_sec_two where bill_no = '13819145656') b
    on a.SEC_MR_CENT_ID = b.SEC_MR_CENT_ID
    where a.p_day = b.p_day and ((a.in_time < b.in_time and a.out_time > b.in_time) or (b.in_time < a.in_time and b.out_time > a.in_time))
    order by a.p_day

    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.SEC_MR_CENT_ID, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from
    (select * from temp_two_hzcompare_two where bill_no = '19558107600') a
    join
    (select * from temp_two_hzcompare_two where bill_no = '13819145656') b
    on a.grid_id = b.grid_id
    where a.p_day = b.p_day and ((a.in_time < b.in_time and a.out_time > b.in_time) or (b.in_time < a.in_time and b.out_time > a.in_time))
    order by a.p_day

-- 基站数据
    create table temp_two_hzcompare_lac as
    select * from dwfu_hive_db.I_TPOS_TRAIL_D where p_day='20220704' and bill_no in ('19558107600', '13819145656')

    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.lac_ci, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from
    (select * from temp_two_hzcompare_lac where bill_no = '19558107600') a
    join
    (select * from temp_two_hzcompare_lac where bill_no = '13819145656') b
    on a.lac_ci = b.lac_ci
    where (a.in_time < b.in_time and a.out_time > b.in_time) or (b.in_time < a.in_time and b.out_time > a.in_time)
    order by a.in_time


-- 使用张帆的二级栅格（7月4号）匹配7月4号的所有人
    -- 先把7月4号这天的所有人的栅格转换为二级栅格
    create table temp_grid_0704_sec as
    select b.SEC_MR_CENT_ID, a.* from (select * from dwfu_hive_db.I_TPOS_TRAIL_GRID_D where p_day = '20220704' and p_city = '3301') a
    join dwfu_hive_db.I_CDM_SEC_MR_RELA b
    on a.grid_id = b.id

    -- // TODO two days
    create table temp_grid_0704_sec_two as
    select b.SEC_MR_CENT_ID, a.* from (select * from dwfu_hive_db.I_TPOS_TRAIL_GRID_D where p_day in ('20220707', '20220708') and p_city = '3301') a
    join dwfu_hive_db.I_CDM_SEC_MR_RELA b
    on a.grid_id = b.id

    -- 关联与张帆在同一时间断内栅格有联系的人
    create table temp_zhangfan_connection as
    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.SEC_MR_CENT_ID, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from temp_grid_0704_sec a
    join (select * from temp_two_hzcompare_sec where bill_no = '19558107600') b
    on a.SEC_MR_CENT_ID = b.SEC_MR_CENT_ID
    where (a.in_time < b.in_time and a.out_time > b.in_time) or (b.in_time < a.in_time and b.out_time > a.in_time)

    -- // TODO two days
    create table temp_zhangfan_connection_two as
    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.SEC_MR_CENT_ID, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from temp_grid_0704_sec_two a
    join (select * from temp_two_hzcompare_sec_two where bill_no = '19558107600') b
    on a.p_day = b.p_day and a.SEC_MR_CENT_ID = b.SEC_MR_CENT_ID
    where (a.in_time < b.in_time and a.out_time > b.in_time) or (b.in_time < a.in_time and b.out_time > a.in_time)

    -- // TODO three days
    create table temp_zhangfan_connection_three as
    select a.bill_no as a_bill_no, b.bill_no as b_bill_no, a.grid_id, a.in_time as a_in_time, b.in_time as b_in_time, a.out_time as a_out_time, b.out_time as b_out_time from (select * from dwfu_hive_db.I_TPOS_TRAIL_GRID_D where p_day in ('20220706', '20220707', '20220708') and p_city = '3301') a
    join (select * from temp_two_hzcompare_three where bill_no = '19558107600') b
    on a.p_day = b.p_day and a.grid_id = b.grid_id
    where (a.in_time < b.in_time and a.out_time > b.in_time) or (b.in_time < a.in_time and b.out_time > a.in_time)

    -- 校验手机号
    create table temp_zhangfan_connection_check as
    select * from temp_zhangfan_connection
    where length(a_bill_no)=11 
    and substr(a_bill_no,1,1)=1 
    and a_bill_no regexp '1[0-9]{10}'
    and a_bill_no <> '19558107600'

    -- // TODO two days
    create table temp_zhangfan_connection_check_two as
    select * from temp_zhangfan_connection_two
    where length(a_bill_no)=11 
    and substr(a_bill_no,1,1)=1 
    and a_bill_no regexp '1[0-9]{10}'
    and a_bill_no <> '19558107600'

    -- 获取张帆关联标的所有信息
        -- 没有限定时间的数据来约10万
        select * from temp_zhangfan_connection_check
        -- 限定2022-07-04 08:00:00-2022-07-04 22:12:04数据量约4万
        select * from temp_zhangfan_connection_check where a_in_time > '2022-07-04 08:00:00' and a_out_time < '2022-07-04 22:12:04'
        -- 限定出现次数不止一次并且两个人之间的总栅格时间大于半小时
        create table temp_zhangfan_connection_check_time as
        select *, 
        case 
        when a_in_time <= b_in_time and a_out_time <= b_out_time then unix_timestamp(a_out_time) - unix_timestamp(b_in_time)
        when a_in_time <= b_in_time and a_out_time >= b_out_time then unix_timestamp(b_out_time) - unix_timestamp(b_in_time)
        when a_in_time >= b_in_time and a_out_time <= b_out_time then unix_timestamp(a_out_time) - unix_timestamp(a_in_time)
        when a_in_time >= b_in_time and a_out_time >= b_out_time then unix_timestamp(b_out_time) - unix_timestamp(a_in_time) 
        end duration
        from temp_zhangfan_connection_check

        -- // TODO three days duration
        create table temp_zhangfan_connection_three_time as
        select *, 
        case 
        when a_in_time <= b_in_time and a_out_time <= b_out_time then unix_timestamp(a_out_time) - unix_timestamp(b_in_time)
        when a_in_time <= b_in_time and a_out_time >= b_out_time then unix_timestamp(b_out_time) - unix_timestamp(b_in_time)
        when a_in_time >= b_in_time and a_out_time <= b_out_time then unix_timestamp(a_out_time) - unix_timestamp(a_in_time)
        when a_in_time >= b_in_time and a_out_time >= b_out_time then unix_timestamp(b_out_time) - unix_timestamp(a_in_time) 
        end duration
        from temp_zhangfan_connection_three

        select a_bill_no from temp_zhangfan_connection_check_time group by a_bill_no having sum(duration) > 1800

        create table temp_zhangfan_connection_check_time_result as
        select * from temp_zhangfan_connection_check_time 
        where a_bill_no in (select a_bill_no from temp_zhangfan_connection_check_time group by a_bill_no having count(a_bill_no) > 1 and sum(duration) > 1800)

        select * from temp_zhangfan_connection_check_time_result order by a_bill_no

        -- 张帆移动数据'2022-07-04 9:24:28'到'2022-07-04 10:04:50'的伴随用户
        select * from temp_zhangfan_connection_check_time 
        where a_bill_no in 
        (
            select a_bill_no from temp_zhangfan_connection_check_time
            where '2022-07-04 09:24:28' <=  b_in_time and b_out_time <= '2022-07-04 10:04:50'
            group by a_bill_no having count(a_bill_no) > 2
        )

        -- 张帆移动数据'2022-07-04 9:24:28'到'2022-07-04 10:04:50'的伴随用户，栅格数量大于2
        select * from temp_zhangfan_connection_check_time 
        where a_bill_no in 
        (
            select a_bill_no from temp_zhangfan_connection_check_time
            where '2022-07-04 09:24:28' <=  b_in_time and b_out_time <= '2022-07-04 10:04:50'
            group by a_bill_no having count(distinct SEC_MR_CENT_ID) > 2
        )

        -- // TODO two days
        select * from temp_zhangfan_connection_check_two 
        where a_bill_no in 
        (
            select a_bill_no from temp_zhangfan_connection_check_two
            where ('2022-07-07 22:00:00' <=  b_in_time and b_out_time <= '2022-07-07 24:00:00') or ('2022-07-08 22:00:00' <=  b_in_time and b_out_time <= '2022-07-08 24:00:00')
            group by a_bill_no having count(distinct SEC_MR_CENT_ID) >= 3
        )

        -- // TODO three days
        select * from temp_zhangfan_connection_three
        where a_bill_no in
        (
            select a_bill_no from temp_zhangfan_connection_three
            where ('2022-07-06 22:00:00' <=  b_in_time and b_out_time <= '2022-07-06 24:00:00') or ('2022-07-07 22:00:00' <=  b_in_time and b_out_time <= '2022-07-07 24:00:00') or ('2022-07-08 22:00:00' <=  b_in_time and b_out_time <= '2022-07-08 24:00:00')
            group by a_bill_no having count(distinct grid_id) >= 3
        )
        order by a_bill_no, a_in_time

        select partition_name, PARTITION_DESCRIPTION, PARTITION_EXPRESSION, table_rows from dwfu_hive_db.I_UIDCT_ALL_HOST_DNS_D

        select *, substr(a_in_time, 1, 10) from temp_zhangfan_connection_three_time
        where a_bill_no in
        (
            select a_bill_no from temp_zhangfan_connection_three_time
            where 8 <= hour(b_in_time) and hour(b_in_time) <= 24 and 8 <= hour(a_in_time) and hour(a_in_time)
            group by substr(a_in_time, 1, 10), a_bill_no
            having sum(duration) >= 3600 and count(distinct grid_id) >= 3
        )
        order by a_bill_no, a_in_time

