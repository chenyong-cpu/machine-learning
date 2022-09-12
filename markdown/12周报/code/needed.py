from LAC import LAC


# 返回一个人名list，可能需要对list进行处理
def lac_username(sentences: str) -> list:
    user_name_list = []
    lac = LAC(mode="lac")
    lac_result = lac.run(sentences)
    for index, lac_label in enumerate(lac_result[1]):
        if lac_label == "PER":
            user_name_list.append(lac_result[0][index])
    return user_name_list


# 对地址进行分类，'ten_type'包含10个地址，传入包含'detailedaddress'和'13个grade'的pandas数组
def split2ten(kdfg_dz_df):
    columns = list(kdfg_dz_df.columns)
    columns.append('ten_type')
    kdfg_dz_df = kdfg_dz_df.reindex(columns=columns)
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"校|大学|小学|初中|高中|学院|学生|幼儿园|中学|教职|教学|教师|学生"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '学校'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"政府|法院|局|检察院|医院|卫生院|机构|服务中心|领导|人武|党校|消防|站|部"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '其它机构'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"公司|集团|总部|企业|政企|移动|联通|电信|药业"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '独立企业'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"工业园|厂|科技园|创意园|生产基地|产业园|厂|开发|加工|基地|设计院"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '工业园区'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"市场|汽车城|菜场|商场"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '专业市场'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"商住"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '商住两用'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"大厦|商业|商务|中心|金座|商城|大楼|银行|信用|国际|科技"), na=False) & kdfg_dz_df['ten_type'].isnull() & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '商业楼宇'
    
    kdfg_dz_df.loc[kdfg_dz_df['detailedaddress'].str.contains((r"店|超市|宾馆|旅馆|小吃|餐|广场"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '沿街店铺'
    kdfg_dz_df.loc[kdfg_dz_df['grade_8'].isnull() & kdfg_dz_df['grade_9'].isnull() & kdfg_dz_df['grade_10'].isnull() & kdfg_dz_df['grade_11'].isnull() & kdfg_dz_df['grade_12'].isnull() & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '沿街店铺'
    
    kdfg_dz_df.loc[kdfg_dz_df['grade_5'].str.contains((r".*村$"), na=False) & kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '农村'

    kdfg_dz_df.loc[kdfg_dz_df['ten_type'].isnull(), 'ten_type'] = '小区'
                                   
    print("小区数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == '小区'].shape[0])
    print("农村数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == '农村'].shape[0])
    print("学校数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == "学校"].shape[0])
    print("其它机构数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == '其它机构'].shape[0])
    print("沿街店铺数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == "沿街店铺"].shape[0])
    print("独立企业数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == '独立企业'].shape[0])
    print("商业楼宇数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == '商业楼宇'].shape[0])
    print("专业市场数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == "专业市场"].shape[0])
    print("商住两用数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == '商住两用'].shape[0])
    print("工业园区数量：", kdfg_dz_df[kdfg_dz_df['ten_type'] == "工业园区"].shape[0])
    
    return kdfg_dz_df
