-- //TODO 测试数据集
create table temp_smalltable_20220706 (
    province string,
    line string,
    station string,
    station_num string,
    station_code string,
    id string,
    lng_bd string,
    lat_bd string
)row format delimited fields terminated by ',' stored as orcfile;