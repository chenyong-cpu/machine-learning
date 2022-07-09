-- 经纬度转换为栅格
-- cast(floor((longitude_bd-0.000441)/(0.00045)) as string) ||'_'|| cast(floor((latitude_bd-0.000381)/(0.00045)) as string)

-- 销售通话信息
select * from dwfu_hive_db.I_TPOS_ADDRESS_GRID_M
where p_mon = '202206' and work_city_name = '杭州市' and work_days >= 15 and bill_no in ('13685785719','13645811573','13732215686','15088792376','15268120039','15868129823','15957189758','15968824043','18458187810')

-- 销售工作地信息，发现'13645811573'这一手机号码不满足条件
select * from dwfu_hive_db.I_TPOS_ADDRESS_GRID_M
where p_mon = '202206' and work_city_name = '杭州市' and work_days >= 15 and  bill_no in ('13685785719','13645811573','13732215686','15088792376','15268120039','15868129823','15957189758','15968824043','18458187810')