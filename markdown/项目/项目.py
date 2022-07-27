import pandas as pd
import numpy as np
import math
import datetime
import time
import os
import re
from multiprocessing import Process, Manager
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

kdfg_dz_df0 = pd.read_csv('./滨江.csv')
#插入各个层级
kdfg_dz_df0.columns = ['detailedaddress', 'prefecture_id', 'prefecture_name', 'county_id', 'county_name', 'township_id', 'township_name', 'addresslevel', 'id', 'name', 'road_id', 'road_name', 'village_id', 'village_name', 'block_id', 'block_name', 'building_id', 'building_name', 'unit_id', 'unit_name', 'floor_id', 'floor_name', 'door_id', 'door_name','p_day','p_city']
kdfg_dz_df = kdfg_dz_df0.reindex(columns=['detailedaddress', 'prefecture_id', 'prefecture_name', 'county_id', 'county_name', 'township_id', 'township_name', 'addresslevel', 'id', 'name', 'road_id', 'road_name', 'village_id', 'village_name', 'block_id', 'block_name', 'building_id', 'building_name', 'unit_id', 'unit_name', 'floor_id', 'floor_name', 'door_id', 'door_name','p_day','p_city', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark'])

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

#将building_name里面的汉字数字转换为阿拉伯数字，可以完成0-99之间的替换
#使用loc()定位相关行列，使用contains划定范围，使用正则匹配，最后用lambda函数进行替换
#contains要匹配多个条件使用正则可以实现
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
kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"^\d*$",'')

# // TODO 这里

#拆分road_name，例如：西园八路10号拆分为西园八路和10号，分别填充到grade_61,grade_62
kdfg_dz_df['grade_61'] = kdfg_dz_df['road_name'].str.split(r"\d+",expand=True)[0]
kdfg_dz_df.loc[kdfg_dz_df['road_name'].str.contains(('-1$'),na = False),'grade_61'] = '-1'
kdfg_dz_df['grade_62'] = kdfg_dz_df.apply(lambda x: x['road_name'].replace(x['grade_61'],''),axis=1)


#对road_name进行分级
#将以村结尾的放在grade_5
kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"村$"),na = False),'grade_5'] = kdfg_dz_df['grade_61']
#将grade_61里面以村结尾的替换为空值（下同）
kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"村$"),na = False),'grade_61'] = ' '
#将以自然村结尾的放在grade_8
kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False),'grade_8'] = kdfg_dz_df['grade_61']
kdfg_dz_df.loc[kdfg_dz_df['grade_61'].str.contains((r"自然村$"),na = False),'grade_61'] = ' '
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
#将以号结尾或者纯数字的放在grade_13
#正则含义：只匹配以号结尾，或者以纯数字结尾的
kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False),'grade_13'] = kdfg_dz_df['grade_62']
kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r".*号$|^\d*$"),na = False),'grade_62'] = ' '
#将以街巷弄路结尾的放在grade_6
kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r"弄$|街$|巷$|路$"),na = False),'grade_6'] = kdfg_dz_df['grade_62']
kdfg_dz_df.loc[kdfg_dz_df['grade_62'].str.contains((r"弄$|街$|巷$|路$"),na = False),'grade_62'] = ' '

kdfg_dz_df[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]

#对village_name进行分级
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"村$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"村$"),na = False),'village_name'] = ' '
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"自然村$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"自然村$"),na = False),'village_name'] = ' '
#将village_name里面的街巷弄路接到grade_61中
kdfg_dz_df['grade_61'] = kdfg_dz_df['grade_61'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"弄$|街$|巷$|路$"),na = False),'village_name'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"弄$|街$|巷$|路$"),na = False),'village_name'] = ' '
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"小区$"),na = False),'grade_8'] = kdfg_dz_df['village_name']
kdfg_dz_df.loc[kdfg_dz_df['village_name'].str.contains((r"小区$"),na = False),'village_name'] = ' '


#将village_name中的社区放在grade_6
temp = kdfg_dz_df['village_name'].str.split(r"([\w]{1,}社区)",expand=True)[1]
kdfg_dz_df['grade_5'] = kdfg_dz_df['grade_5'].str.cat(temp.loc[temp.str.contains((r"社区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将village_name中的社区去除
kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([\w]{1,}社区)",'',regex = True)

try:
    #将village_name中的号放在grade_7
    temp = kdfg_dz_df['village_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
    kdfg_dz_df['grade_7'] = kdfg_dz_df['grade_7'].str.cat(temp.loc[temp.str.contains((r"号"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    
    #将village_name中的号去除
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9-]{1,}号)",'',regex = True)
except:
    pass

try:
    #将village_name中的弄放在grade_6
    temp = kdfg_dz_df['village_name'].str.split(r"(\w{1,}弄)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将village_name中的弄去除
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"(\w{1,}弄)",'',regex = True)
except:
    pass

try:
    #将village_name中的省道放在grade_6
    temp = kdfg_dz_df['village_name'].str.split(r"([0-9]{1,}省道)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"省道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将village_name中的省道去除
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9]{1,}省道)",'',regex = True)
except:
    pass

try:
    #将village_name中的幢放在grade_10
    temp = kdfg_dz_df['village_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
    kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将village_name中的幢去除
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'',regex = True)
except:
    pass
try:
    #将village_name中的单元放在grade_11
    temp = kdfg_dz_df['village_name'].str.split(r"([0-9a-zA-Z]{1,}单元)",expand=True)[1]
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将village_name中的单元去除
    kdfg_dz_df['village_name'] = kdfg_dz_df['village_name'].str.replace(r"([0-9a-zA-Z]{1,}单元)",'',regex = True)
except:
    pass


#将各个字段中未分出去的值填到相应的字段
kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat([kdfg_dz_df['grade_61']],sep='',na_rep='')
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat([kdfg_dz_df['village_name']],sep='',na_rep='')

#将block_name中的线放在grade_6
temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}线)",expand=True)[1]
kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"线"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的线去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}线)",'',regex = True)

try:
    #将block_name中的国道放在grade_6
    temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}国道)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"国道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将block_name中的国道去除
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}国道)",'',regex = True)
except:
    pass

#将block_name中的路放在grade_6
temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}路)",expand=True)[1]
kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的路去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}路)",'',regex = True)

#将block_name中的弄放在grade_6
temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}弄)",expand=True)[1]
kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的弄去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}弄)",'',regex = True)

#将block_name中的号放在grade_13
"""错误：可以将[0-9]修改成[0-9-]避免出现*-*号分出去一般"""
temp = kdfg_dz_df['block_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"号"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的号去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9-]{1,}号)",'',regex = True)

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
#将block_name中的期放在grade_9
temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}期)",expand=True)[1]
kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"期"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的期去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}期)",'',regex = True)

#将block_name中的区放在grade_9
temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z东南西北]{1,}区)",expand=True)[1]
kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的区去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z东南西北]{1,}区)",'',regex = True)

#将block_name中的幢放在grade_10
temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的幢去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'',regex = True)

#将block_name中的单元放在grade_11
temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}单元)",expand=True)[1]
kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的单元去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}单元)",'',regex = True)

#将block_name中的层放在grade_12
temp = kdfg_dz_df['block_name'].str.split(r"([0-9a-zA-Z]{1,}层)",expand=True)[1]
kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将block_name中的层去除
kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9a-zA-Z]{1,}层)",'',regex = True)

try:
    #将block_name中的出租屋放在grade_13
    temp = kdfg_dz_df['block_name'].str.split(r"(.{1,}自建房)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将block_name中的出租屋去除
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"(.{1,}自建房)",'',regex = True)
except:
    pass

try:
    #将block_name中的室放在grade_13
    temp = kdfg_dz_df['block_name'].str.split(r"([0-9]{1,}室)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将block_name中的室去除
    kdfg_dz_df['block_name'] = kdfg_dz_df['block_name'].str.replace(r"([0-9]{1,}室)",'',regex = True)
except:
    pass

# #将各个字段中未分出去的值填到相应的字段
# kdfg_dz_df.loc[kdfg_dz_df['grade_8'].isnull(),'grade_8'] = kdfg_dz_df[kdfg_dz_df['block_name'].notnull()]['block_name']
#将各个字段中未分出去的值填到相应的字段
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat([kdfg_dz_df['block_name']],sep='',na_rep='')

kdfg_dz_df[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]

#将building_name里的街道回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}街道)",expand=True)[1]
kdfg_dz_df['grade_4'] = kdfg_dz_df['grade_4'].str.cat(temp.loc[temp.str.contains((r"街道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的街道去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}街道)",'')

#将building_name里的路回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}路)",expand=True)[1]
kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的路去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}路)",'')

#将building_name里的村回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}村)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的村去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}村)",'')
#将building_name中以村委村头开始的保留
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"^村(?!委|头)",'')

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
#将building_name里的建筑、小区回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}厦)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"厦"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的建筑、小区去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}厦)",'')

temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}苑)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"苑"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的苑去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}苑)",'')

temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}公寓)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"公寓"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的苑去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}公寓)",'')

temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}局)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"局"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的局去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}局)",'')

temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}公司)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"公司"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的公司去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}公司)",'')

try:
    temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}厂)",expand=True)[1]
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"厂"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将building_name中的厂去除
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}厂)",'')
except:
    pass

try:
    temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}园区)",expand=True)[1]
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"园区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将building_name中的厂去除
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}园区)",'')
except:
    pass

temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}小区)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"小区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的小区去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}小区)",'')

temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}(?<!幢|号)店)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"店"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的店去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}(?<!幢|号)店)",'')


try:
    #将building_name里的自建房回填到对应层级
    temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}自建房$)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将building_name中的自建房去除
    kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}自建房$)",'')
except:
    pass
#将building_name里的单元回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"([0-9-]{1,}单元)",expand=True)[1]
kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的单元去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9-]{1,}单元)",'')

#将building_name里的楼、层回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}楼)",expand=True)[1]
kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"楼"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的楼去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9]{1,}楼)",'')

temp = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}层)",expand=True)[1]
kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的层去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9]{1,}层)",'')

#将building_name里的室回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"([0-9a-zA-Z]{1,}室)",expand=True)[1]
kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的室去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9a-zA-Z]{1,}室)",'')

#将building_name里的井回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"(.{1,}井)",expand=True)[1]
kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"井"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的井去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"(.{1,}井)",'')

#将building_name里的号回填到对应层级
temp = kdfg_dz_df['building_name'].str.split(r"([0-9-]{1,}号)",expand=True)[1]
kdfg_dz_df['grade_13'] = temp.str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将building_name中的号去除
kdfg_dz_df['building_name'] = kdfg_dz_df['building_name'].str.replace(r"([0-9-]{1,}号)",'')

#将building_name中的楼和幢保留,其他字段结尾的统统丢到13中
temp1 = kdfg_dz_df['building_name'].str.split(r"([0-9]{1,}幢)",expand=True)
"""错误点"""#代码需要修复，会漏掉数据
#修正V1.0修复了building_name回填会覆盖原有grade_10中字段的问题
kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp1[1],sep='',na_rep='')
kdfg_dz_df['grade_10'] = kdfg_dz_df['building_name'].str.cat(temp1.loc[temp1[0].str.contains((r"楼$|幢"),na = False)],sep='',na_rep='')
kdfg_dz_df['grade_10'] = kdfg_dz_df['building_name'].str.cat(temp1.loc[temp1[3].str.contains((r"楼$|幢"),na = False)],sep='',na_rep='')


#将temp1中的楼和幢结尾的全部替代为空
temp1[0] = temp1[0].str.replace(r"(.{1,}楼$)|(.{1,}幢$)",'')
#将剩下的不以楼和幢结尾的放到grade_13中
kdfg_dz_df['grade_13'] = temp1[0].str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')
kdfg_dz_df['grade_13'] = temp1[2].str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')
kdfg_dz_df['grade_13'] = temp1[4].str.cat(kdfg_dz_df['grade_13'],sep='',na_rep='')

try:
    #将unit_name里的路回填到对应层级
    temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}路)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将unit_name中的路去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}路)",'')
except:
    pass
#将unit_name里的村回填到对应层级
temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}村)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将unit_name中的村去除
kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}村)",'')
#将unit_name中以村委村头开始的保留
kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"^村(?!委|头)",'')

try:
    #将unit_name里的弄回填到对应层级
    temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}弄)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将unit_name中的弄去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}弄)",'')
except:
    pass

#将unit_name里的区、组、排、期回填到对应层级
try:
    temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}区)",expand=True)[1]
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"区"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
except:
    pass
try:
    temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}组)",expand=True)[1]
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"组"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
except:
    pass
try:
    temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}排)",expand=True)[1]
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"排"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
except:
    pass
try:
    temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}期)",expand=True)[1]
    kdfg_dz_df['grade_9'] = kdfg_dz_df['grade_9'].str.cat(temp.loc[temp.str.contains((r"期"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
except:
    pass
#将unit_name中的区、组、排、期去除
kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}区)|([0-9]{1,}组)|([0-9]{1,}排)|([0-9]{1,}期)",'')

try:
    #将unit_name里的自建房回填到对应层级
    temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}自建房$)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"自建房"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将unit_name中的自建房去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}自建房$)",'')
except:
    pass


#将unit_name里的幢回填到对应层级
temp = kdfg_dz_df['unit_name'].str.split(r"([0-9a-zA-Z]{1,}幢)",expand=True)[1]
kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].str.cat(temp.loc[temp.str.contains((r"幢"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将unit_name中的幢去除
kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9a-zA-Z]{1,}幢)",'')

#将unit_name里的楼层回填到对应层级
temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}楼)",expand=True)[1]
kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"楼"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将unit_name中的楼去除
kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}楼)",'')
temp = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}层)",expand=True)[1]
kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat(temp.loc[temp.str.contains((r"层"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将unit_name中的层去除
kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"([0-9]{1,}层)",'')

try:
    #将unit_name里的井回填到对应层级
    temp = kdfg_dz_df['unit_name'].str.split(r"(井道)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"井道"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将unit_name中的井去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(井道)",'')
except:
    pass

try:
    temp = kdfg_dz_df['unit_name'].str.split(r"(.{1,}井)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"井"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将unit_name中的井去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(.{1,}井)",'')
except:
    pass

try:
    #将unit_name里的()回填到对应层级
    temp = kdfg_dz_df['unit_name'].str.split(r"(（.{1,}）)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将unit_name中的()去除
    kdfg_dz_df['unit_name'] = kdfg_dz_df['unit_name'].str.replace(r"(（.{1,}）)",'')
except:
    pass

#将grade_11中的单元保留,其他字段结尾的统统丢到13中
temp2 = kdfg_dz_df['unit_name'].str.split(r"([0-9]{1,}单元)",expand=True)
'''错误点'''
#修改V1.0，改正了unit_name回填覆盖原有的单元
kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp2[1],sep='',na_rep='')
kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp2.loc[temp2[0].str.contains((r"单元$"),na = False)],sep='',na_rep='')


#将temp2中的单元结尾的全部替代为空
temp2[0] = temp2[0].str.replace(r"单元$",'')
#将剩下的不以楼和幢结尾的放到grade_13中
kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp2[0],sep='',na_rep='')
kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp2[2],sep='',na_rep='')


kdfg_dz_df[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]

#将floor_name里的路回填到对应层级
try:
    temp = kdfg_dz_df['floor_name'].str.split(r"(.{1,}路)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将floor_name中的路去除
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(.{1,}路)",'')
except:
    pass

try:    
    #将floor_name里的村回填到对应层级
    temp = kdfg_dz_df['floor_name'].str.split(r"(.{1,}村)",expand=True)[1]
    kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将floor_name中的村去除
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(.{1,}村)",'')
except:
    pass

try:
    #将floor_name里的室回填到对应层级
    temp = kdfg_dz_df['floor_name'].str.split(r"([0-9]{1,}室)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"室"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将floor_name中的室去除
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"([0-9]{1,}室)",'')
except:
    pass

try:
    #将floor_name里的单元回填到对应层级
    temp = kdfg_dz_df['floor_name'].str.split(r"([0-9]{1,}单元)",expand=True)[1]
    kdfg_dz_df['grade_11'] = kdfg_dz_df['grade_11'].str.cat(temp.loc[temp.str.contains((r"单元"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将floor_name中的单元去除
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"([0-9]{1,}单元)",'')
except:
    pass

try:
    #将floor_name里的()回填到对应层级
    temp = kdfg_dz_df['floor_name'].str.split(r"(（.{1,}）)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"（.{1,}）"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将floor_name中的()去除
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"(（.{1,}）)",'')
except:
    pass

try:
    #将floor_name里的号回填到对应层级
    temp = kdfg_dz_df['floor_name'].str.split(r"([0-9]{1,}号)",expand=True)[1]
    kdfg_dz_df['grade_13'] = kdfg_dz_df['grade_13'].str.cat(temp.loc[temp.str.contains((r"号"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将floor_name中的室去除
    kdfg_dz_df['floor_name'] = kdfg_dz_df['floor_name'].str.replace(r"([0-9]{1,}号)",'')
except:
    pass

#将各个字段中未分出去的值填到相应的字段
kdfg_dz_df['grade_12'] = kdfg_dz_df['grade_12'].str.cat([kdfg_dz_df['floor_name']],sep='',na_rep='')


kdfg_dz_df[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]

try:
    #将door_name里的弄回填到对应层级
    temp = kdfg_dz_df['door_name'].str.split(r"([0-9]{1,}弄)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"弄"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将door_name中的弄去除
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"([0-9]{1,}弄)",'')
    #将door_name里的路回填到对应层级
except:
    pass

try:
    temp = kdfg_dz_df['door_name'].str.split(r"(.*(?<!公)路)",expand=True)[1]
    kdfg_dz_df['grade_6'] = kdfg_dz_df['grade_6'].str.cat(temp.loc[temp.str.contains((r"路"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将door_name中的路去除
    kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.*路)",'')
except:
    pass
#将door_name里的村回填到对应层级
temp = kdfg_dz_df['door_name'].str.split(r"(.*村)",expand=True)[1]
kdfg_dz_df['grade_8'] = kdfg_dz_df['grade_8'].str.cat(temp.loc[temp.str.contains((r"村"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
#将door_name中的村去除
kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"(.*村)",'')
#将door_name中以村委村头开始的保留
kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].str.replace(r"^村(?!委|头)",'')

#将DOOR_NAME中剩下的和grade_13进行合并
kdfg_dz_df['door_name'] = kdfg_dz_df['door_name'].map(lambda x: str(x))
kdfg_dz_df ['grade_13'] = kdfg_dz_df['grade_13'].str.cat(kdfg_dz_df['door_name'],sep='',na_rep='')



kdfg_dz_df[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]

#将13中的号放在grade_10中，如果grade_5有村且grade_10为空
#v1.0
#kdfg_dz_df.loc[kdfg_dz_df['grade_5'].str.contains(r"村",na = False),'grade_10'] = kdfg_dz_df['grade_10'].str.cat(kdfg_dz_df.loc[kdfg_dz_df['grade_13'].str.findall(r"[0-9]{1,}号"),'grade_13'],sep='',na_rep='')

#v2.0(杜)
kdfg_dz_df.loc[kdfg_dz_df['grade_5'].str.contains('村',na=False)&kdfg_dz_df['grade_10'].str.contains('',na=False),'grade_10'] = kdfg_dz_df.loc[kdfg_dz_df['grade_13'].str.contains('[0-9]{1,}号',na = False),'grade_13'].apply(lambda x:re.findall(r'[0-9-]{1,}号',x)[0])
kdfg_dz_df['grade_10'] = kdfg_dz_df['grade_10'].astype(str)
kdfg_dz_df['grade_10'] = kdfg_dz_df.apply(lambda x: x['grade_10'].replace('nan',''),axis=1)
kdfg_dz_df['grade_13'] = kdfg_dz_df.apply(lambda x: x['grade_13'].replace(x['grade_10'],''),axis=1)

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

#合并原来的表
#删除除grade之外的字段
kdfg_dz_df.drop(kdfg_dz_df.columns[:26], axis=1, inplace=True)
kdfg_dz_df1 = pd.read_csv('/root/data/hangzhou1_tonglu_1.csv')
kdfg_dz_df1.columns = ['detailedaddress', 'prefecture_id', 'prefecture_name', 'county_id', 'county_name', 'township_id', 'township_name', 'addresslevel', 'id', 'name', 'road_id', 'road_name', 'village_id', 'village_name', 'block_id', 'block_name', 'building_id', 'building_name', 'unit_id', 'unit_name', 'floor_id', 'floor_name', 'door_id', 'door_name','p_day','p_city']
#向外合并表
kdfg_dz_df2 = pd.merge(kdfg_dz_df,kdfg_dz_df1,left_index=True,right_index=True,how='outer')


"""
将grade_13中的号放回grade_8中为空且grade_6中有路的grade_7中
"""
kdfg_dz_df2['grade_8'] = kdfg_dz_df2['grade_8'].astype(str)
kdfg_dz_df2['grade_8'] = kdfg_dz_df2['grade_8'].str.replace(r'\\N','',regex = True)
kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].str.replace(r'NaN','',regex = True)
kdfg_dz_df2.loc[kdfg_dz_df2['grade_6'].str.contains('路|巷|街|道|弄',na=False)&kdfg_dz_df2['grade_8'].str.contains('^((?![\u4e00-\u9fa5]).)*$',na=False)&kdfg_dz_df2['grade_8'].str.contains('^((?![\u4e00-\u9fa5]).)*$',na=False),'grade_7'] = kdfg_dz_df2.loc[kdfg_dz_df2['grade_13'].str.contains('[0-9-]{1,}号',na = False),'grade_13'].apply(lambda x:re.findall(r'[0-9-]{1,}号',x)[0])
kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].astype(str)
kdfg_dz_df2['grade_13'] = kdfg_dz_df2['grade_13'].astype(str)

# kdfg_dz_df2['grade_7'] = kdfg_dz_df2['grade_7'].map(lambda x: str(x))
kdfg_dz_df2['grade_7'] = kdfg_dz_df2.apply(lambda x: x['grade_7'].replace(r'nan',''),axis=1)
kdfg_dz_df2['grade_13'] = kdfg_dz_df2.apply(lambda x: x['grade_13'].replace(x['grade_7'],''),axis=1)

"""将grade_8中以街结尾的放入grade_5"""
try:
    temp = kdfg_dz_df2['grade_8'].str.split(r"(\w*街$)",expand=True)[1]
    kdfg_dz_df2['grade_6'] = kdfg_dz_df2['grade_6'].str.cat(temp.loc[temp.str.contains((r"街"),na = False)],sep='',na_rep='')#拼接方式为：拼接符号为空格，空值使用空值进行拼接
    #将grade_8中的街去除
    kdfg_dz_df2['grade_8'] = kdfg_dz_df2['grade_8'].str.replace(r"(\w*街$)",'')
except:
    pass

kdfg_dz_df2[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]

sample1_yuhang = kdfg_dz_df2.sample(n=10000,random_state=None,axis=0)
sample1_yuhang[['detailedaddress','village_name','building_name','block_name', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10','grade_11', 'grade_12', 'grade_13','remark']]