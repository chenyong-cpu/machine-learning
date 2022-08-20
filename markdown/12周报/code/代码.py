import pandas as pd
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

def type_conversion(kdfg_dz_df):
    #类型转换
    kdfg_dz_df['grade_1'] = kdfg_dz_df['grade_1'].map(lambda x: str(x))
    kdfg_dz_df['grade_2'] = kdfg_dz_df['grade_2'].map(lambda x: str(x))
    kdfg_dz_df['grade_3'] = kdfg_dz_df['grade_3'].map(lambda x: str(x))
    kdfg_dz_df['grade_4'] = kdfg_dz_df['grade_4'].map(lambda x: str(x))
    kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].map(lambda x: str(x))
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].map(lambda x: str(x))
    kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].map(lambda x: str(x))
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].map(lambda x: str(x))
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].map(lambda x: str(x))
    kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].map(lambda x: str(x))
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].map(lambda x: str(x))
    kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].map(lambda x: str(x))
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].map(lambda x: str(x))
    kdfg_dz_df['remark'] = kdfg_dz_df['remark'].map(lambda x: str(x))
    #将英文括号转为中文括号
    kdfg_dz_df['road_name'] = kdfg_dz_df['road_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['road_name'] = kdfg_dz_df['road_name'].str.replace(r"\)",'）',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"\)",'）',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"\)",'）',regex = True)
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"\)",'）',regex = True)
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"\)",'）',regex = True)
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"\)",'）',regex = True)
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"\(",'（',regex = True)
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"\)",'）',regex = True)
    """
    将各级的括号放在remark里面
    """
    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['road_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['road_name'] = kdfg_dz_df['road_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass

    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['village_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass

    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['block_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass

    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['building_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass

    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['unit_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass

    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['floor_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass

    try:
        #将以（）的放在remark中
        temp = kdfg_dz_df['door_name'].str.split(r"(（.*）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r".*"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将（）去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(（.*）)",'',regex = True)
    except:
        pass
    print('type conversion done')
    return kdfg_dz_df

def keyword_conversion(kdfg_dz_df):
    try:
        #将block_name里面的汉字数字转换为阿拉伯数字，可以完成0-99之间的替换
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('二十','2'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('三十','3'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('四十','4'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('五十','5'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('六十','6'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('七十','7'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('八十','8'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('九十','9'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('一','1'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('二','2'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('三','3'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('四','4'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('五','5'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('六','6'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('七','7'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('八','8'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('九','9'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('十','1'))
        kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元'),'block_name'] = kdfg_dz_df[kdfg_dz_df['block_name'].str.contains(r'期|区|苑|幢|组|街|单元')]['block_name'].apply(lambda x:x.replace('零','0'))
    except:
        print('block_name里面的汉字数字转换为阿拉伯数字 error')
    try:
        #将village_name里面的汉字数字转换为阿拉伯数字，可以完成0-99之间的替换
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('二十','2'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('三十','3'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('四十','4'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('五十','5'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('六十','6'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('七十','7'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('八十','8'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('九十','9'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('一','1'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('二','2'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('三','3'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('四','4'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('五','5'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('六','6'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('七','7'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('八','8'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('九','9'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('十','1'))
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元'),'village_name'] = kdfg_dz_df[kdfg_dz_df['village_name'].str.contains(r'期|苑|幢|组|街|单元')]['village_name'].apply(lambda x:x.replace('零','0'))
    except:
        print('village_name里面的汉字数字转换为阿拉伯数字 error')
    #将building_name里面的汉字数字转换为阿拉伯数字，可以完成0-99之间的替换
    #使用loc()定位相关行列，使用contains划定范围，使用正则匹配，最后用lambda函数进行替换
    #contains要匹配多个条件使用正则可以实现
    try:
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('二十','2'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('三十','3'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('四十','4'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('五十','5'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('六十','6'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('七十','7'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('八十','8'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('九十','9'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('一','1'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('二','2'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('三','3'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('四','4'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('五','5'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('六','6'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('七','7'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('八','8'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('九','9'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('十','1'))
        kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元'),'building_name'] = kdfg_dz_df[kdfg_dz_df['building_name'].str.contains(r'期|区|号|苑|幢|组|街|弄|单元')]['building_name'].apply(lambda x:x.replace('零','0'))
    except:
        print('building_name里面的汉字数字转换为阿拉伯数字 error')
    #将block_name里面的替换
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(?<=[0-9])楼",'层',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"#楼",'幢',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"#",'幢',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"号楼",'幢',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"栋",'幢',regex = True)
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(?<=[a-zA-Z])座",'幢',regex = True)

    #将village_name里面的替换（清洗：统一幢和层）
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"(?<=[0-9])楼|F",'层',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"#楼",'幢',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"#",'幢',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"号楼",'幢',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"栋",'幢',regex = True)
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"(?<=[a-zA-Z])座",'幢',regex = True)

    #将building_name里面的替换（清洗：统一幢和层）
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"#楼",'幢')
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"#",'幢')
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"号楼",'幢')
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"栋",'幢')
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(?<=[a-zA-Z])座",'幢')
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"F",'层',regex = True)
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"第",'',regex = True)


    #将unit_name里面的替换（清洗：统一幢和层）
    # rfl = ["#楼","#","号楼","栋","(?<=[a-zA-Z])座"]
    # for i in rfl:
    #     kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(i,'幢')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"#楼",'幢')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"#",'幢')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"号楼",'幢')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"栋",'幢')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(?<=[a-zA-Z])座",'幢')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"F",'层')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"^第",'')
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"^\d*$",'')

    #将floor_name里面的替换（清洗：统一幢和层）
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"#楼",'幢')
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"#",'幢')
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"号楼",'幢')
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"栋",'幢')
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(?<=[a-zA-Z])座",'幢')
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"F",'层')
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"^第",'')

    # 变更
    #将door_name里面的替换（清洗：统一幢和层）
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"#楼",'幢')
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"#",'幢')
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"号楼",'幢')
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"栋",'幢')
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(?<=[a-zA-Z])座",'幢')
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"F",'层')
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"^第",'')
    # 变更结束
    print('keyword conversion done')
    return kdfg_dz_df

def roadname_process(kdfg_dz_df):
    #对road_name进行分级

    #拆分road_name，例如：西园八路10号拆分为西园八路和10号，分别填充到grade_61,grade_62

    kdfg_dz_df['grade_61'] = kdfg_dz_df['road_name'].str.split(r"\d+",expand=True)[0]
    kdfg_dz_df.loc[kdfg_dz_df['road_name'].str.contains(('-1$'),na = False),'grade_61'] = '-1'
    kdfg_dz_df['grade_62'] = kdfg_dz_df.apply(lambda x: x['road_name'].replace(x['grade_61'],''),axis=1)


    # 个人理解中存在的问题：
    # 村和自然村从字上存在逻辑包含，所以应当先匹配自然村，然后再匹配村，否则会将自然村结尾数据放到第五级中去，不知是否有特殊原因？
    # 理论上对road_name进行拆分之后，需要对grade_62先进行处理？（因为数字和之前的关键字存在相关性？）
    # 如西园八路10号 西元八路应该填到grade6 而10号应该填到grade7
    # 而xx自然村xx号 xx自然村填到grade_8 xx号填到grade_10

    #变更


    # 调整 处理比较严格的分类结果 如 西园八路10号 或者xx自然村xx号
    # 先处理grade_62，再处理grade_61
    kdfg_dz_df.loc[(kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False))&(kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False)),'grade_10'] = kdfg_dz_df['grade_62']
    kdfg_dz_df.loc[(kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False))&(kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False)),'grade_62'] = ' '
    # 调整  联合grade_61中匹配弄 街 巷 路匹配grade_62中路号
    kdfg_dz_df.loc[(kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False))&(kdfg_dz_df['grade_61'].str.contains((r"弄$|街$|巷$|路$"),na = False)),'grade_7'] = kdfg_dz_df['grade_62']
    kdfg_dz_df.loc[(kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False))&(kdfg_dz_df['grade_61'].str.contains((r"弄$|街$|巷$|路$"),na = False)),'grade_7'] = ' '
    # #其余没有前缀的和之前一样的规则进行匹配

    # 调整 先匹配自然村结尾的，然后匹配村结尾的
    # 将以自然村结尾的放在grade_8
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False),'grade_8'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False),'grade_61'] = ' '
    #将以村结尾的放在grade_5
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"村$"),na = False),'grade_5'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"村$"),na = False),'grade_61'] = ' '

    # # 调整 从grade_61中匹配弄 街 巷 路
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"弄$|街$|巷$|路$"),na = False),'grade_6'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"弄$|街$|巷$|路$"),na = False),'grade_61'] = ' '

    # 变更结束

    # 存疑部分代码进行注释

    # #将以村结尾的放在grade_5
    # kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"村$"),na = False),'grade_5'] = kdfg_dz_df['grade_61']
    # #将grade_61里面以村结尾的替换为空值（下同）
    # kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"村$"),na = False),'grade_61'] = ' '
    # # 将以自然村结尾的放在grade_8
    # kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False),'grade_8'] = kdfg_dz_df['grade_61']
    # kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False),'grade_61'] = ' '


    #将以小区结尾的放在grade_8
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"小区$"),na = False),'grade_8'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"小区$"),na = False),'grade_61'] = ' '
    #将以社区结尾的放在grade_5
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"社区$"),na = False),'grade_5'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"社区$"),na = False),'grade_61'] = ' '
    #将以幢结尾的放在grade_10
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"幢$"),na = False),'grade_10'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"幢$"),na = False),'grade_61'] = ' '
    #将以单元结尾的放在grade_11
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"单元$"),na = False),'grade_11'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"单元$"),na = False),'grade_61'] = ' '
    #将以层结尾的放在grade_12
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"层$"),na = False),'grade_12'] = kdfg_dz_df['grade_61']
    kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"层$"),na = False),'grade_61'] = ' '

    # 再对grade_62根据数字进行拆分

    # 将以号结尾或者纯数字的放在grade_13
    # 处理 其余存在多个数字的数据

    # 正则含义：只匹配以号结尾，或者以纯数字结尾的
    kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False),'grade_13'] = kdfg_dz_df['grade_62']
    kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False),'grade_62'] = ' '

    #将以街巷弄路结尾的放在grade_6
    kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r"弄$|街$|巷$|路$"),na = False),'grade_6'] = kdfg_dz_df['grade_62']
    kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r"弄$|街$|巷$|路$"),na = False),'grade_62'] = ' '
    print('road name done')
    return kdfg_dz_df

def villagename_process(kdfg_dz_df):
    # 变更

    # 调整 直接匹配以村结尾的数据

    kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"村$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
    kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"村$"),na = False),'village_name'] = ' '

    # 变更结束

    # 存疑部分代码进行注释

    # #对village_name进行分级
    # kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"村$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
    # kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"村$"),na = False),'village_name'] = ' '
    # kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"自然村$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
    # kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"自然村$"),na = False),'village_name'] = ' '
    try:
        #将village_name里面的街巷弄路接到grade_61中
        kdfg_dz_df['grade_61'] = kdfg_dz_df['grade_61'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"弄$|街$|巷$|路$"),na = False),'village_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"弄$|街$|巷$|路$"),na = False),'village_name'] = ' '
        #将village_name里面的小区放到grade_8中
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"小区$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
        kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"小区$"),na = False),'village_name'] = ' '
    except:
        pass

    # 变更 xx号的地址，因为不同层级信息后的xx号代表的意义不同,进行不同层次的回填

    try:
        #将village_name中的号放在grade_7
        # temp = kdfg_dz_df['village_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
        temp = kdfg_dz_df['village_name'].str.split(r"([0-9-]{1,}号)",expand=True)

        # 将xx号之前为自然村的放到grade_10
        #拼接方式为：拼接符号为空格，空值使用空值进行拼接
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"自然村$"),na = False)),1],sep='',na_rep='')
        # 置空，防止误匹配以村为后缀的
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"自然村$"),na = False)),1]=''
        # 将以村 弄 街 巷 路 后的放到  grade_7 
        #拼接方式为：拼接符号为空格，空值使用空值进行拼接
        kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"省道$|村$|弄$|街$|巷$|路$"),na = False)),1],sep='',na_rep='')
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"省道$|村$|弄$|街$|巷$|路$"),na = False)),1]=''
    #     # 将以 楼 后的放到  grade_13
    #     kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"楼$"),na = False))][1],sep='',na_rep='')
    #     temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"楼$"),na = False)),1]=''
        # 将 其他匹配情况 如只有 xx号字段的数据放入grade_7
        kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False)),1],sep='',na_rep='')

        # 可能丢失一部分难以判断的xx号数据，如果保守一点的话，则将除了能够分辨出需要回填到grade_10中的数据，其余的都放到grade_7（将上面两行注释，下面一行取消注释）
        # kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[temp[1].str.contains((r"号"),na = False)][1],sep='',na_rep='')

        #将village_name中的号去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9-]{1,}号)",'',regex = True)
    except:
        print('village_name xx号 cut error')

    # 变更结束

    try:
        #将village_name中的社区放在grade_6
        temp = kdfg_dz_df['village_name'].str.split(r"([\w]{1,}社区)",expand=True)[1]
        kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].str.cat(temp.loc[temp.str.contains((r"社区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将village_name中的社区去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([\w]{1,}社区)",'',regex = True)
    except:
        print('village_name 社区 cut error')


    try:
        #将village_name中的村放在grade_5
        temp = kdfg_dz_df['village_name'].str.split(r"(.{1,}村)",expand=True)[1]
        kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将village_name中的村去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"(\w{1,}村)",'',regex = True)
    except:
        print('village_name 村 cut error')

    try:
        #将village_name中的弄放在grade_6
        temp = kdfg_dz_df['village_name'].str.split(r"(\w{1,}弄)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将village_name中的弄去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"(\w{1,}弄)",'',regex = True)
    except:
        print('village_name 弄 cut error')

    try:
        #将village_name中的省道放在grade_6
        temp = kdfg_dz_df['village_name'].str.split(r"([0-9]{1,}省道)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"省道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将village_name中的省道去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9]{1,}省道)",'',regex = True)
    except:
        print('village_name 省道 cut error')

    try:
        #将village_name中的期放在grade_10
        temp = kdfg_dz_df['village_name'].str.split(r"([0-9]{1,}期)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"期"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    except:
         print('village_name split xx期 error')

    try:
        #将village_name中的幢放在grade_10
        temp = kdfg_dz_df['village_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将village_name中的幢去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'',regex = True)
    except:
        print('village_name 幢 cut error')
    try:
        #将village_name中的单元放在grade_11
        temp = kdfg_dz_df['village_name'].str.split(r"([0-9a-zA-Z]{1,}单元)",expand=True)[1]
        kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将village_name中的单元去除
        kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9a-zA-Z]{1,}单元)",'',regex = True)
    except:
        print('village_name 单元 cut error')



    # 变更

    # 将上面的内容替换为''后，可能又出现了以小区或者其他关键字进行结尾的数据，所以再进行一次匹配如 xx路xx号，第一次不匹配，然后经过上述匹配后，会变为xx小区,则可以进行匹配
    # 将village_name里面的街巷弄路接到grade_61中 可能存在重复问题，后续以进行了清洗
    kdfg_dz_df['grade_61'] = kdfg_dz_df['grade_61'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"街$|巷$|路$"),na = False),'village_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"街$|巷$|路$"),na = False),'village_name'] = ' '
    # 小区部分不用再次匹配，默认去除上述匹配后其余数据回填到grade_8


    # sample1.1.3 存在未处理的xx层级信息
    try:
        #将village_name中的期放在grade_10
        temp = kdfg_dz_df['village_name'].str.split(r"([0-9]{1,}层)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    except:
         print('village_name split xx层 error')
    # 变更结束

    #将各个字段中未分出去的值填到相应的字段
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat([kdfg_dz_df['grade_61']],sep='',na_rep='')
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat([kdfg_dz_df['village_name']],sep='',na_rep='')
    print('village name done')
    return kdfg_dz_df

def blockname_process(kdfg_dz_df):
    # 变更
    # block_name 中存在较多的含有 '线' 字的实体名，如建德市周岳铝镁合金制线有限公司、xx线店、xx针线工厂等
    # 存在 含有 '路' 字的实体名 如 大同公路管理站 环城北路商铺 政法路幼儿园
    # 处理 实体名 的数据（建德数据） 放入grade_8
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r"幼儿园$|商铺$|管理站$|公司$|工厂$|店$"),na = False),'block_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r"幼儿园$|商铺$|公司$|工厂$|店$"),na = False),'block_name'] = ''

    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r"工区$|卫生室$|市场$|宿舍楼$|宿舍$"),na = False),'block_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r"工区$|卫生室$|市场$|宿舍楼$|宿舍$"),na = False),'block_name'] = ''

    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r"门$|杆$|杆子$|杆上$|馆$"),na = False),'block_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r"门$|杆$|杆子$|杆上$|馆$"),na = False),'block_name'] = ''
    # 变更结束

    # 变更 
    # 建德 中  xx号 和 xx-x号
    try:
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9-]{1,}号)",expand=True)

        # 将xx号之前为自然村的放到grade_10
        #拼接方式为：拼接符号为空格，空值使用空值进行拼接
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"自然村$"),na = False))][1],sep='',na_rep='')
        # 置空，防止误匹配以村为后缀的
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"自然村$"),na = False)),1]=''
        # 将以村 弄 街 巷 路 后的放到  grade_7 
        #拼接方式为：拼接符号为空格，空值使用空值进行拼接
        kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"省道$|村$|弄$|街$|巷$|路$"),na = False))][1],sep='',na_rep='')
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"省道$|村$|弄$|街$|巷$|路$"),na = False)),1]=''
        # 将 其他匹配情况 如只有 xx号字段的数据放入grade_10
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))][1],sep='',na_rep='')

        #将block_name中的号去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9-]{1,}号)",'',regex = True)
    except:
        print('block_name x-x号 cut error')


    # 变更结束


    #将block_name中的线放在grade_6
    try:
        temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}线)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"线"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的线去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}线)",'',regex = True)
    except:
        print('block_name 线 cut error')

    try:
        #将block_name中的国道放在grade_6
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}国道)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"国道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的国道去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}国道)",'',regex = True)
    except:
        pass
    try:
        #将block_name中的路放在grade_6
        temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}路)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的路去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}路)",'',regex = True)
    except:
        pass

    try:
        #将block_name中的弄放在grade_6
        temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}弄)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的弄去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}弄)",'',regex = True)
    except:
        pass






    # 存疑部分

    # #将block_name中的号放在grade_13
    # """错误：可以将[0-9]修改成[0-9-]避免出现*-*号分出去一般"""
    # temp = kdfg_dz_df['block_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
    # kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"号"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    # #将block_name中的号去除
    # kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}-[0-9]{1,}号)",'',regex = True)

    # 结束

    #将block_name中的组放在grade_9
    try:
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}组)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"组"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的组去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}组)",'',regex = True)
    except:
        pass

    try:
        #将block_name中的排放在grade_9
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}排)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"排"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的排去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}排)",'',regex = True)
    except:
        pass
    try:
        #将block_name中的期放在grade_9
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}期)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"期"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的期去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}期)",'',regex = True)
    except:
        pass

    try:
        #将block_name中的区放在grade_9
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z东南西北]{1,}区)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的区去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z东南西北]{1,}区)",'',regex = True)
    except:
        pass
    try:
        #将block_name中的幢放在grade_10
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的幢去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'',regex = True)
    except:
        pass
    try:
        #将block_name中的单元放在grade_11
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}单元)",expand=True)[1]
        kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的单元去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}单元)",'',regex = True)
    except:
        pass
    try:
        #将block_name中的层放在grade_12
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}层)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的层去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}层)",'',regex = True)
    except:
        pass

    # 变更
    # 自建房应该属于标志物？放到grade_8
    try:
        #将block_name中的自建房放在grade_8
        temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}自建房)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的自建房去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}自建房)",'',regex = True)
    except:
        pass
    try:
        #将block_name中的安置房放在grade_8
        temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}安置房)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"安置房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的安置房去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}安置房)",'',regex = True)
    except:
        pass
    # 变更结束

    # 存疑部分

    # try:
    #     #将block_name中的出租屋放在grade_13
    #     temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}自建房)",expand=True)[1]
    #     kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #     #将block_name中的出租屋去除
    #     kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}自建房)",'',regex = True)
    # except:
    #     pass

    # 结束

    try:
        #将block_name中的室放在grade_13
        temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}室)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将block_name中的室去除
        kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}室)",'',regex = True)
    except:
        pass


    # 变更

    # 处理上述的信息后，将带模糊信息描述 的数据（建德数据） 放入grade_8
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'block_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['block_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'block_name'] = ''


    # kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat([kdfg_dz_df['block_name']],sep='',na_rep='')
    # 变更结束
    try:
        #将各个字段中未分出去的值填到相应的字段
        kdfg_dz_df.loc[kdfg_dz_df['grade_8'].isnull(),'grade_8'] = kdfg_dz_df[kdfg_dz_df['block_name'].notnull()]['block_name']
    except:
        pass
    # 将各个字段中未分出去的值填到相应的字段
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat([kdfg_dz_df['block_name']],sep='',na_rep='')
    print('block name done')
    return kdfg_dz_df

def buildingname_process(kdfg_dz_df):
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.replace('nan','')
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.replace('nan','')
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].astype(str)
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.replace(r'\\N','',regex = True)
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.replace('nan','')

    # 同样先进行xx号数据的处理，因为其和文本前关键词具有较强关联,由于已经处理了block_name，实体已经部分回填到了grade_8中，所以对于只有xx号的
    # 联合grade_8进行匹配分级
    # 变更
    try:
        #将building_name里的号回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9-]{1,}号)",expand=True)
        kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]=='')&(kdfg_dz_df['grade_8']=='')&(kdfg_dz_df['grade_9']=='')&(kdfg_dz_df['grade_6']!=''), 1],sep='',na_rep='')
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]=='')&(kdfg_dz_df['grade_8']=='')&(kdfg_dz_df['grade_9']=='')&(kdfg_dz_df['grade_6']!=''), 1]=''

        # 没有截断实体信息的xx号回填到grade_7
        kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]!='')&(temp[0].str.contains((r"([弄|街|巷|路])$"),na = False)),1],sep='',na_rep='')
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]!='')&(temp[0].str.contains((r"([弄|街|巷|路])$"),na = False)),1]=''
        # 带有截断实体信息的xx号回填到grade_10并且将截断信息回填到grade_8 .*(?<![弄|街|巷|路])$
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]!='')&(temp[0].str.contains((r"(?<![弄|街|巷|路])$"),na = False)), 1],sep='',na_rep='')
        # 将截断实体回填到grade_8
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]!='')&(temp[0].str.contains((r"(?<![弄|街|巷|路])$"),na = False)), 0],sep='',na_rep='')
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0]!='')&(temp[0].str.contains((r"(?<![弄|街|巷|路])$"),na = False)), 1]=''

        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False)), 1],sep='',na_rep='')
        #将building_name中的号去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9-]{1,}号)",'')
    except:
        print('building_name xx号 cut error')
    # 变更结束

    # 变更
    # sample1.1.5 将building_name中的街道回填到grade_8中，由于原始数据中存在着grade_4层级信息，导致后续回填时产生数据的覆盖，同时x规定中x街道的层级属于4
    # 但是 杭州市桐庐县瑶琳镇瑶琳路瑶琳街道王玉强门口 这条数据的街道在xx路之后，应当放到哪个层级？
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}街道)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"街道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的街道去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}街道)",'')
    except:
        print('building_name cut xx街道 error')
    # sample 1.1 处理xx区
    try:
        #将building_name中的区放在grade_9
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9a-zA-Z东南西北]{1,}区)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的区去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9a-zA-Z东南西北]{1,}区)",'',regex = True)
    except:
        pass
    # sample 1.1 处理2c
    try:
        #将building_name中的区放在grade_9
        temp = kdfg_dz_df['building_name'].str.split(r"^([0-9]{1,})([a-zA-Z]{1,})$",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"^([0-9]{1,})([a-zA-Z]{1,})$"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的区去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"^([0-9]{1,})([a-zA-Z]{1,})$",'',regex = True)
    except:
        pass
    # sample 1.1 处理 2 纯数字
    try:
        #将building_name中的纯数字放在grade_10
        temp = kdfg_dz_df['building_name'].str.split(r"^([0-9]{1,})$",expand=True)[1]
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"^([0-9]{1,})$"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的纯数字去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"^([0-9]{1,})$",'',regex = True)
    except:
        pass
    # 变更结束

    # #将building_name里的街道回填到对应层级
    # temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}街道)",expand=True)[1]
    # kdfg_dz_df['grade_4'] = kdfg_dz_df['grade_4'].str.cat(temp.loc[temp.str.contains((r"街道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    # #将building_name中的街道去除
    # kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}街道)",'')

    try:
        #将building_name里的路回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}路)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的路去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}路)",'')
    except:
        print('building_name 路 cut error')
    try:
        #将building_name里的村回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}村)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的村去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}村)",'')
        #将building_name中以村委村头开始的保留
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"^村(?!委|头)",'')
    except:
        print('building_name 村 cut error')

    try:
        #将building_name里的弄回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}弄)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的弄去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9]{1,}弄)",'')
    except:
        pass

    try:
        #将building_name里的巷回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}巷)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"巷"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的巷去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}巷)",'')
    except:
        pass
    try:
        #将building_name里的建筑、小区回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}厦)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"厦"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的建筑、小区去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}厦)",'')
    except:
        print('building_name 厦 cut error')
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}苑)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"苑"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的苑去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}苑)",'')
    except:
        print('building_name 苑 cut error')
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}公寓)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"公寓"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的苑去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}公寓)",'')
    except:
        print('building_name 公寓 cut error')
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}局)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"局"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的局去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}局)",'')
    except:
        print('building_name 局 cut error')
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}公司)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"公司"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的公司去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}公司)",'')
    except:
        pass

    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}厂)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"厂"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的厂去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}厂)",'')
    except:
        pass

    # 变更
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}家园)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"家园"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的xx家园去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}家园)",'')
    except:
        pass

    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}家)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"家"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的xx家去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}家)",'')
    except:
        pass

    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}房)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的xx房去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}房)",'')
    except:
        pass
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}商铺)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"商铺"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的xx家园去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}商铺)",'')
    except:
        pass
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}超市)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"超市"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的xx家园去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}超市)",'')
    except:
        print('building_name 超市 cut error')
    # 变更结束


    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}园区)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"园区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的厂去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}园区)",'')
    except:
        pass

    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}小区)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"小区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的小区去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}小区)",'')
    except:
        pass
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}(?<!幢|号)店)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"店"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的店去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}(?<!幢|号)店)",'')
    except:
        print('building_name 店 cut error')


    try:
        #将building_name里的自建房回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}自建房$)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的自建房去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}自建房$)",'')
    except:
        pass
    try:
        #将building_name里的单元回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9-]{1,}单元)",expand=True)[1]
        kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的单元去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9-]{1,}单元)",'')
    except:
        print('building_name 单元 cut error')
    try:
        #将building_name里的楼、层回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}楼)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"楼"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的楼去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9]{1,}楼)",'')
    except:
        pass
    try:
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}层)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的层去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9]{1,}层)",'')
    except:
        print('building_name 层 cut error')
    try:
        #将building_name里的室回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9a-zA-Z]{1,}室)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的室去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9a-zA-Z]{1,}室)",'')
    except:
        print('building_name 室 cut error')
    try:
        #将building_name里的井回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}井)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"井"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将building_name中的井去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}井)",'')
    except:
        print('building_name 井 cut error')


    # #将building_name里的号回填到对应层级
    # temp = kdfg_dz_df['building_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
    # kdfg_dz_df['grade_13'] = temp.str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    # #将building_name中的号去除
    # kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9-]{1,}号)",'')





    try:
        # sample 1.1
        #将building_name中的楼和幢保留,其他字段结尾的统统丢到13中
        temp1 = kdfg_dz_df['building_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)
        """错误点"""#代码需要修复，会漏掉数据
        #修正V1.0修复了building_name回填会覆盖原有grade_10中字段的问题
        # kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp1[1],sep='',na_rep='')

        # 变更 将xx幢之前的xx楼放入grade_8中 类似宿舍楼xx幢 宿舍楼放入grade_8, xx幢放入grade_10
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp1.loc[(temp1[0].str.contains((r"楼$"),na = False))&(temp1[1].str.contains((r"幢"),na = False)), 0],sep='',na_rep='')
        # 将没有xx幢 并且以楼结尾的描述性地址 放入grade_10 进大门二排中楼
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp1.loc[(temp1[0].str.contains((r"楼$"),na = False))&(temp1[1].isnull()), 0],sep='',na_rep='')
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp1.loc[(temp1[1].str.contains((r"幢"),na = False)), 1],sep='',na_rep='')
        # 变更结束
        # kdfg_dz_df['grade_10'] = kdfg_dz_df['building_name'].str.cat(temp1.loc[temp1[0].str.contains((r"楼$|幢"),na = False)],sep='',na_rep='')
        # kdfg_dz_df['grade_10'] = kdfg_dz_df['building_name'].str.cat(temp1.loc[temp1[3].str.contains((r"楼$|幢"),na = False)],sep='',na_rep='')
        #将temp1中的楼和幢结尾的全部替代为空
        temp1[0] = temp1[0].str.replace(r"(.{1,}楼$)|(.{1,}幢$)",'')
        #sample 1.1
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}楼)|(.{1,}幢)",'')
    except:
        print('building_name 楼和幢 cut error')


    # 变更
    # sample1.1.2 可能存在203等室号，以严格匹配的方法，如果之前那的步骤全部都处理完后，只剩余203这类纯数字，那么就将其放入grade_13中
    try:
        #将building_name里的xxx回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"^(\d{1,})$",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"(\d)"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"^(\d{1,})$",'')
    except:
        print('building_name split xxx(302) error')

    # sample1.1.7 添加工业园识别切分
    try:
        #将building_name里的xxx回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}工业园)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"工业园"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}工业园)",'')
    except:
        print('building_name split xx工业园 error')


    # sample1.1.10 添加宿舍识别切分
    try:
        #将building_name里的xxx回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}宿舍)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"宿舍"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}宿舍)",'')
    except:
        print('building_name split xx宿舍 error')


    # sample1.1.11添加xx厂识别切分
    try:
        #将building_name里的xxx回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}[厂|场])",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"[厂|场]"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}[厂|场])",'')
    except:   
        print('building_name split xx厂 error')


    # sample1.1.12添加xx-xx
    try:
        #将building_name里的xxx回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"(\d{1,}-\d{1,})",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"\d"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将building_name中的xxx去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(\d{1,}-\d{1,})",'')
    except:   
        print('building_name split 20-30 error')


    # sample1.1.15 处理xx组
    try:
        #将building_name里的xx组回填到对应层级
        temp = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}组)",expand=True)[1]
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"组"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将building_name中的xxx去除
        kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9]{1,}组)",'')
    except:   
        print('building_name split xx组 error')

    # 处理上述的信息后，将带模糊信息描述 的数据（建德数据） 放入grade_8
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'building_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['building_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'building_name'] = ''


    #将剩下的不以楼和幢结尾的放到remark中
    kdfg_dz_df['remark'] = temp1[0].str.cat(kdfg_dz_df['remark'],sep='',na_rep='')
    kdfg_dz_df['remark'] = temp1[2].str.cat(kdfg_dz_df['remark'],sep='',na_rep='')
    kdfg_dz_df['remark'] = temp1[4].str.cat(kdfg_dz_df['remark'],sep='',na_rep='')
    # 变更结束
    

    # #将剩下的不以楼和幢结尾的放到grade_13中
    # kdfg_dz_df['grade_13'] = temp1[0].str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')
    # kdfg_dz_df['grade_13'] = temp1[2].str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')
    # kdfg_dz_df['grade_13'] = temp1[4].str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')
    print('building name done')
    return kdfg_dz_df

def unitname_process(kdfg_dz_df):
    # 变更 对于unit_name中存在的xx村xx号xx 类信息，进行xx号的切分与信息回填
    # 修正 sample1.1

    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9-]{1,}号)",expand=True)
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"自然村$"),na = False)),1],sep='',na_rep='')
        # 避免自然村和村的层级便准混淆
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"自然村$"),na = False)),1]=''
        # xx号之间为以xx路结尾的数据，把xx号回填到grade_7
        kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"[弄|街|巷|路|村]$"),na = False)),1],sep='',na_rep='')
        temp.loc[(temp[1].str.contains((r"号"),na = False))&(temp[0].str.contains((r"[弄|街|巷|路|村]$"),na = False)),1]=''
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[(temp[1].str.contains((r"号"),na = False)), 1],sep='',na_rep='')
        #将unit_name中的号去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9-]{1,}号)",'')
    except:
        print("unit_name xx号 cut error")
    # 修正 sample1.1
    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"^(\d{1,})$",expand=True)[1]
        kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"(\d)"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"^(\d{1,})$",'')
    except:
        print('unit_name split xxx(302) error')

    # 变更结束


    try:
        #将unit_name里的路回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}路)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的路去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}路)",'')
    except:
        print('unit_name split xx路 error')

    try:
        #将unit_name里的村回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}村)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的村去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}村)",'')
        #将unit_name中以村委村头开始的保留
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"^村(?!委|头)",'')
    except:
        print('unit_name split xx村 error')

    try:
        #将unit_name里的弄回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}弄)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的弄去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}弄)",'')
    except:
        print('unit_name split xx弄 error')

    #将unit_name里的区、组、排、期回填到对应层级
    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}区)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    except:
        print('unit_name split xx区 error')
    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}组)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"组"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    except:
         print('unit_name split xx组 error')
    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}排)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"排"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    except:
         print('unit_name split xx排 error')
    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}期)",expand=True)[1]
        kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"期"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    except:
         print('unit_name split xx期 error')
    #将unit_name中的区、组、排、期去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}区)|([0-9]{1,}组)|([0-9]{1,}排)|([0-9]{1,}期)",'')

    try:
        #将unit_name里的自建房回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}自建房$)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的自建房去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}自建房$)",'')
    except:
         print('unit_name split 自建房$ error')


    try:
        #将unit_name里的幢回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的幢去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'')
    except:
        print('unit_name split 幢 error')
    try:
        #将unit_name里的楼层回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}楼)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"楼"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的楼去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}楼)",'')
    except:
        print('unit_name split 楼 error')
    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}层)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的层去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}层)",'')
    except:
        print('unit_name split 层 error')

    try:
        #将unit_name里的井回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"(井道)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"井道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的井去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(井道)",'')
    except:
         print('unit_name split xx井道 error')

    try:
        temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}井)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"井"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的井去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}井)",'')
    except:
         print('unit_name split xx井 error')
    # 变更
    try:
        #将floor_name里的室回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}室)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的室去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}室)",'')
    except:
        print('unit_name split xx室 error')

    try:
        #将unit_name里的()回填到对应层级
        temp = kdfg_dz_df['unit_name'].str.split(r"(（.{1,}）)",expand=True)[1]
        kdfg_dz_df['reamrk'] = kdfg_dz_df['reamrk'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的()去除
        kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(（.{1,}）)",'')
    except:
         print('unit_name split （.{1,}） error')

    # 变更结束

    # try:
    #     #将unit_name里的()回填到对应层级
    #     temp = kdfg_dz_df['unit_name'].str.split(r"(（.{1,}）)",expand=True)[1]
    #     kdfg_dz_df['reamrk'] = kdfg_dz_df['reamrk'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #     #将unit_name中的()去除
    #     kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(（.{1,}）)",'')
    # except:
    #      print('unit_name split （.{1,}） error')

    #将grade_11中的单元保留,其他字段结尾的统统丢到13中
    temp2 = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}单元)",expand=True)
    '''错误点'''
    #修改V1.0，改正了unit_name回填覆盖原有的单元
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp2[1],sep='',na_rep='')
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp2.loc[temp2[0].str.contains((r"单元$"),na = False)],sep='',na_rep='')


    #将temp2中的单元结尾的全部替代为空
    temp2[0] = temp2[0].str.replace(r"单元$",'')


    # 变更
    # 处理上述的信息后，将带模糊信息描述 的数据（建德数据） 放入grade_8
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['unit_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'unit_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['unit_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'unit_name'] = ' '
    #将剩下的不以楼和幢结尾的放到remark中
    kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp2[0],sep='',na_rep='')
    kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp2[2],sep='',na_rep='')
    # 变更结束
    print('unit name done')
    # #将剩下的不以楼和幢结尾的放到grade_13中
    # kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp2[0],sep='',na_rep='')
    # kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp2[2],sep='',na_rep='')
    return kdfg_dz_df

def floorname_process(kdfg_dz_df):
    # 将floor_name里的路回填到对应层级
    try:
        temp = kdfg_dz_df['floor_name'].str.split(r"(.{1,}路)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将floor_name中的路去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(.{1,}路)",'')
    except:
        print('floor_name split xx路 error')

    try:    
        #将floor_name里的村回填到对应层级
        temp = kdfg_dz_df['floor_name'].str.split(r"(.{1,}村)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将floor_name中的村去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(.{1,}村)",'')
    except:
        print('floor_name split xx村 error')

    try:
        #将floor_name里的室回填到对应层级
        temp = kdfg_dz_df['floor_name'].str.split(r"([0-9]{1,}室)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的室去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"([0-9]{1,}室)",'')
    except:
        print('floor_name split xx室 error')

    try:
        #将floor_name里的单元回填到对应层级
        temp = kdfg_dz_df['floor_name'].str.split(r"([0-9]{1,}单元)",expand=True)[1]
        kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将floor_name中的单元去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"([0-9]{1,}单元)",'')
    except:
        print('floor_name split xx单元 error')

    # 变更
    try:
        #将floor_name里的()回填到对应层级
        temp = kdfg_dz_df['floor_name'].str.split(r"(（.{1,}）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将floor_name中的()去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(（.{1,}）)",'')
    except:
        print('floor_name split （.{1,}） error')
    # 变更结束

    # try:
    #     #将floor_name里的()回填到对应层级
    #     temp = kdfg_dz_df['floor_name'].str.split(r"(（.{1,}）)",expand=True)[1]
    #     kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #     #将floor_name中的()去除
    #     kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(（.{1,}）)",'')
    # except:
    #     print('floor_name split （.{1,}） error')

    try:
        #将floor_name里的号回填到对应层级
        temp = kdfg_dz_df['floor_name'].str.split(r"([0-9]{1,}号)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"号"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将floor_name中的室去除
        kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"([0-9]{1,}号)",'')
    except:
        print('floor_name split xx号 error')

    #将各个字段中未分出去的值填到相应的字段
    kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat([kdfg_dz_df['floor_name']],sep='',na_rep='')
    print('door name done')
    return kdfg_dz_df

def doorname_process(kdfg_dz_df):
    # 变更
    try:
        #将door_name里的()回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(（.{1,}）)",expand=True)[1]
        kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将floor_name中的()去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(（.{1,}）)",'')
    except:
        print('floor_name split （.{1,}） error') 
    # 变更结束

    try:
        #将door_name里的弄回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"([0-9]{1,}弄)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将door_name中的弄去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9]{1,}弄)",'')
        #将door_name里的路回填到对应层级
    except:
         print('door_namee split xx弄 error')

    try:
        temp = kdfg_dz_df['door_name'].str.split(r"(.*(?<!公)路)",expand=True)[1]
        kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将door_name中的路去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.*路)",'')
    except:
        print(r'door_name split ?<!公)路 error')
    
    try:
        #将door_name里的村回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.*村)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将door_name中的村去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.*村)",'')
        #将door_name中以村委村头开始的保留
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"^村(?!委|头)",'')
    except:
        print('door_name split xx村 error')


    # 变更
    # sample1.1.14 处理xx超市
    try:
        #将door_name里的公司回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}超市)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"超市"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的自建房去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}超市)",'')
    except:
        print('door_name split xx超市 error')    

    try:
        #将door_name里的幢回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
        kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将unit_name中的幢去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'')
    except:
        print('door_name split xx幢 error')
    
    try:
        # 将door_name里的楼层回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"([0-9]{1,}楼)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"楼"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将door_name中的楼去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9]{1,}楼)",'')
    except:
        print('door_name split xx楼 error')
        
    try:
        temp = kdfg_dz_df['door_name'].str.split(r"([0-9]{1,}层)",expand=True)[1]
        kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将door_name中的层去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9]{1,}层)",'')
    except:
        print('door_name split xx层 error')
    try:
        #将door_name里的号回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"号"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将door_name中的号去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9-]{1,}号)",'')
        #将door_name里的路回填到对应层级
    except:
         print('door_namee split xx弄 error')
    try:
        #将door_name里的室回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"([0-9]{1,}室)",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的室去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9]{1,}室)",'')
    except:
        print('door_name split xx室 error')
    # sample1.1 处理xx-xx
    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"^([0-9]{1,})-([0-9]{1,})$",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"(\d)"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"^([0-9]{1,})-([0-9]{1,})$",'')
    except:
        print('door_name split (302-1) error')
    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"^(\d{1,})$",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"(\d)"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"^(\d{1,})$",'')
    except:
        print('door_name split xxx(302) error')

    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(\d{1,})$",expand=True)[1]
        kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"(\d)"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(\d{1,})$",'')
    except:
        print('door_name split xxx(余汗根102) error')


    try:
        #将door_name里的自建房回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}自建房)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的自建房去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}自建房)",'')
    except:
        print('door_name split xx自建房 error')

    # sample1.1.4 处理xx出租房
    try:
        #将door_name里的自建房回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}出租房)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"出租房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的自建房去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}出租房)",'')
    except:
        print('door_name split xx出租房 error')

    # sample1.1.7 处理xx公司
    try:
        #将door_name里的公司回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}公司)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"公司"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的自建房去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}公司)",'')
    except:
        print('door_name split xx公司 error')    


    # sample1.1.9 处理xx厂
    try:
        #将door_name里的公司回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}厂)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"厂"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的自建房去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}厂)",'')
    except:
        print('door_name split xx厂 error') 
    # sample1.1.17 处理xx体育馆    
    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}体育馆)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"体育馆"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}体育馆)",'')
    except:
        print('door_name split xxx体育馆 error')

    # sample1.1.18 处理xx基地    
    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}基地)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"基地"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}基地)",'')
    except:
        print('door_name split xxx基地 error')

    # sample1.1.18 处理xx文具    
    try:
        #将door_name里的xxx回填到对应层级
        temp = kdfg_dz_df['door_name'].str.split(r"(.{1,}文具)",expand=True)[1]
        kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"文具"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        # 将floor_name中的xxx去除
        kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.{1,}文具)",'')
    except:
        print('door_name split xxx文具 error')
    # 变更结束

    # 处理上述的信息后，将带模糊信息描述 的数据（建德数据） 放入grade_8
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['door_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'door_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    kdfg_dz_df.loc[kdfg_dz_df['door_name'].str.contains((r'前|后|左|右|边|上|对面|旁'),na = False),'door_name'] = ' '

    #将DOOR_NAME中剩下的和grade_13进行合并
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].map(lambda x: str(x))
    kdfg_dz_df['remark'] = kdfg_dz_df['remark'].str.cat(kdfg_dz_df['door_name'],sep='',na_rep='')
    print('door name done')
    return kdfg_dz_df

def none_value_unify(kdfg_dz_df):
    #将2-4级中为nan的回填上对应的name
    kdfg_dz_df.loc[kdfg_dz_df['grade_2'].str.contains('nan',na=False),'grade_2'] = kdfg_dz_df[kdfg_dz_df['prefecture_name'].notnull()]['prefecture_name']
    kdfg_dz_df.loc[kdfg_dz_df['grade_3'].str.contains('nan',na=False),'grade_3'] = kdfg_dz_df[kdfg_dz_df['county_name'].notnull()]['county_name']
    kdfg_dz_df.loc[kdfg_dz_df['grade_4'].str.contains('nan',na=False),'grade_4'] = kdfg_dz_df[kdfg_dz_df['township_name'].notnull()]['township_name']
    #将各grade中得nan字段替换为空
    kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].str.replace('nan','')
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.replace('nan','')
    kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.replace('nan','')
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.replace('nan','')
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.replace('nan','')
    kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.replace('nan','')
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.replace('nan','')
    kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.replace('nan','')
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.replace('nan','')
    # 变更
    kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].str.replace(' ','')
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.replace(' ','')
    kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.replace(' ','')
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.replace(' ','')
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.replace(' ','')
    kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.replace(' ','')
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.replace(' ','')
    kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.replace(' ','')
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.replace(' ','')
    # 变更结束
    print('none_value_unify done')
    return kdfg_dz_df

def word_merge(sentence, max_ngram_length = 4):
    '''合并文本中连续重复的词'''
    final_merge_sent = sentence
    max_ngram_length = min(max_ngram_length, len(sentence))
    for i in range(max_ngram_length, 0, -1):
        start = 0
        end = len(final_merge_sent) - i + 1
        ngrams = []
        while start < end:
            ngrams.append(final_merge_sent[start: start + i])
            start += 1
        result = []
        for cur_word in ngrams:
            result.append(cur_word)
            if len(result) > i:
                pre_word = result[len(result) - i - 1]
                if pre_word == cur_word:
                    for k in range(i):
                        result.pop()
        cur_merge_sent = ""
        for word in result:
            if not cur_merge_sent:
                cur_merge_sent += word
            else:
                cur_merge_sent += word[-1]
        final_merge_sent = cur_merge_sent
    return final_merge_sent

def word_merge_process(kdfg_dz_df):
    # sample1.1.1
    kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].apply(lambda x: word_merge(x))
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].apply(lambda x: word_merge(x))
    print('word merge process done')
    return kdfg_dz_df

def merge_data(kdfg_dz_df, data_file_path):
    if not os.path.exists(data_file_path):
        print('file path error')
        return
    kdfg_dz_df1 = pd.read_csv(data_file_path,low_memory=False)
    kdfg_dz_df1.columns = ['detailedaddress', 'prefecture_id', 'prefecture_name', 'county_id', 'county_name', 'township_id', 'township_name', 'addresslevel', 'id', 'name', 'road_id', 'road_name', 'village_id', 'village_name', 'block_id', 'block_name', 'building_id', 'building_name', 'unit_id', 'unit_name', 'floor_id', 'floor_name', 'door_id', 'door_name','p_day','p_city']
    #向外合并表
    kdfg_dz_df2 = pd.merge(kdfg_dz_df,kdfg_dz_df1,left_index=True,right_index=True,how='outer')
    return kdfg_dz_df2

def merge_data_process(kdfg_dz_df2):
    """
    将grade_13中的号放回grade_8中为空且grade_6中有路的grade_7中
    """
    kdfg_dz_df2['grade_8'] = kdfg_dz_df2['grade_8'].astype(str)
    kdfg_dz_df2['grade_8'] = kdfg_dz_df2['grade_8'].str.replace(r'\\N','',regex = True)
    kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].str.replace(r'NaN','',regex = True)

    kdfg_dz_df2['grade_12'] = kdfg_dz_df2['grade_12'].astype(str)
    kdfg_dz_df2['grade_12'] = kdfg_dz_df2['grade_12'].str.replace(r'\\N','',regex = True)
    kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].str.replace(r'NaN','',regex = True)

    # kdfg_dz_df2.loc[kdfg_dz_df2['grade_6'].str.contains('路|巷|街|道|弄',na=False)&kdfg_dz_df2['grade_8'].str.contains('^((?![\u4e00-\u9fa5]).)*$',na=False)&kdfg_dz_df2['grade_8'].str.contains('^((?![\u4e00-\u9fa5]).)*$',na=False),'grade_7'] = kdfg_dz_df2.loc[kdfg_dz_df2['grade_13'].str.contains('[0-9-]{1,}号',na = False),'grade_13'].apply(lambda x:re.findall(r'[0-9-]{1,}号',x)[0])
    kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].astype(str)
    kdfg_dz_df2['grade_13'] = kdfg_dz_df2['grade_13'].astype(str)
    kdfg_dz_df2['grade_13'] = kdfg_dz_df2['grade_13'].str.replace(r'\\N','',regex = True)

    # kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].map(lambda x: str(x))
    kdfg_dz_df2['grade_7'] = kdfg_dz_df2.apply(lambda x: x['grade_7'].replace(r'nan',''),axis=1)
    # kdfg_dz_df2['grade_13'] = kdfg_dz_df2.apply(lambda x: x['grade_13'].replace(x['grade_7'],''),axis=1)

    kdfg_dz_df2['remark'] = kdfg_dz_df2['remark'].astype(str)
    kdfg_dz_df2['remark'] = kdfg_dz_df2['remark'].str.replace(r'\\N','',regex = True)
    kdfg_dz_df2['remark'] = kdfg_dz_df2['remark'].str.replace(r'NaN','',regex = True)
    kdfg_dz_df2['remark'] = kdfg_dz_df2.apply(lambda x: x['remark'].replace(r'nan',''),axis=1)

    """将grade_8中以街结尾的放入grade_5"""
    try:
        temp = kdfg_dz_df2['grade_8'].str.split(r"(\w*街$)",expand=True)[1]
        kdfg_dz_df2['grade_6'] = kdfg_dz_df2['grade_6'].str.cat(temp.loc[temp.str.contains((r"街"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
        #将grade_8中的街去除
        kdfg_dz_df2['grade_8'] = kdfg_dz_df2['grade_8'].str.replace(r"(\w*街$)",'')
    except:
        pass
    # 变更
    b1 = (kdfg_dz_df2['grade_13'].str.contains((r'([0-9]{1,}号)$'),na=False))&(kdfg_dz_df2['grade_8']!='')&(kdfg_dz_df2['grade_10']=='')
    kdfg_dz_df2.loc[b1,'grade_10'] = kdfg_dz_df2.loc[b1,'grade_13']
    kdfg_dz_df2.loc[b1,'grade_13']=''
    b2 = (kdfg_dz_df2['grade_13'].str.contains((r'([0-9]{1,}号)$'),na=False))&(kdfg_dz_df2['grade_8']=='')&(kdfg_dz_df2['grade_10']=='')&(kdfg_dz_df2['grade_7']!='')
    kdfg_dz_df2.loc[b2,'grade_10'] = kdfg_dz_df2.loc[b2,'grade_13']
    kdfg_dz_df2.loc[b2,'grade_13']=''
    b5 = (kdfg_dz_df2['grade_13'].str.contains((r'([0-9]{1,}号)$'),na=False))&(kdfg_dz_df2['grade_8']=='')&(kdfg_dz_df2['grade_7']=='')&(kdfg_dz_df2['grade_10']=='')&(kdfg_dz_df2['grade_5']!='')&(kdfg_dz_df2['grade_6']=='')
    kdfg_dz_df2.loc[b5,'grade_7'] = kdfg_dz_df2.loc[b5,'grade_13']
    kdfg_dz_df2.loc[b5,'grade_13'] = ''
    b3 = (kdfg_dz_df2['grade_10'].str.contains((r'([0-9]{1,}号)$'),na=False))&(kdfg_dz_df2['grade_8']=='')&(kdfg_dz_df2['grade_7']=='')&(kdfg_dz_df2['grade_6']!='')
    kdfg_dz_df2.loc[b3,'grade_7'] = kdfg_dz_df2.loc[b3,'grade_10']
    kdfg_dz_df2.loc[b3,'grade_10']=''
    # 变更结束
    return kdfg_dz_df2

def main_process(kdfg_dz_df, columns_len, file_path, columns):
    kdfg_dz_df = type_conversion(kdfg_dz_df)
    kdfg_dz_df = keyword_conversion(kdfg_dz_df)
    kdfg_dz_df = roadname_process(kdfg_dz_df)
    kdfg_dz_df = villagename_process(kdfg_dz_df)
    kdfg_dz_df = blockname_process(kdfg_dz_df)
    kdfg_dz_df = buildingname_process(kdfg_dz_df)
    kdfg_dz_df = unitname_process(kdfg_dz_df)
    kdfg_dz_df = floorname_process(kdfg_dz_df)
    kdfg_dz_df = doorname_process(kdfg_dz_df)
    kdfg_dz_df = none_value_unify(kdfg_dz_df)
    kdfg_dz_df = word_merge_process(kdfg_dz_df)
    kdfg_dz_df.drop(kdfg_dz_df.columns[:26], axis=1, inplace=True)
    kdfg_dz_df1 = pd.read_csv(file_path,low_memory=False)
    if list(kdfg_dz_df1.columns) != columns:
        kdfg_dz_df1.columns = columns
    kdfg_dz_df2 = pd.merge(kdfg_dz_df1,kdfg_dz_df,left_index=True,right_index=True,how='outer')
    kdfg_dz_df2 = merge_data_process(kdfg_dz_df2)
    kdfg_dz_df2['grade_1']='浙江省'
    return kdfg_dz_df2  

def process_address():
    # 获取文件存储路径
    path = '../data/杭州/'
    path_ls = os.listdir(path)
    pa_ls = list()
    for filename in path_ls:
        if os.path.splitext(filename)[1]==".csv": 
            pa_ls.append(filename)
    # 去除路径中原有错误文件
    pa_ls.pop(7)
    columns = ['detailedaddress', 'prefecture_id', 'prefecture_name', 'county_id', 'county_name', 'township_id',
               'township_name', 'addresslevel', 'id', 'name', 'road_id', 'road_name', 'village_id', 'village_name',
               'block_id', 'block_name', 'building_id', 'building_name', 'unit_id', 'unit_name', 'floor_id', 'floor_name',
               'door_id', 'door_name','p_day','p_city']
    new_columns = ['detailedaddress', 'prefecture_id', 'prefecture_name', 'county_id', 'county_name', 'township_id',
                   'township_name', 'addresslevel', 'id', 'name', 'road_id', 'road_name', 'village_id', 'village_name',
                   'block_id', 'block_name', 'building_id', 'building_name', 'unit_id', 'unit_name', 'floor_id', 'floor_name',
                   'door_id', 'door_name','p_day','p_city', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6',
                   'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']
    for filename in pa_ls:
        print('proces '+filename[:-6])
        kdfg_dz_df0 = pd.read_csv(path+filename,low_memory=False)
        if list(kdfg_dz_df0.columns) != columns:
            kdfg_dz_df0.columns = columns
        kdfg_dz_df = kdfg_dz_df0.reindex(columns=new_columns)
        kdfg_dz_df2 = main_process(kdfg_dz_df, 26, path+filename, columns)
        kdfg_dz_df2.to_csv(path+'test_result/V1_1_'+filename, encoding='utf-8')
        print(filename[:-6]+'done')