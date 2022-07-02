#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
import math
from pyspark.sql.types import ArrayType, StringType,DoubleType


class Point():
    def __init__(self,long,lat):
        self.long = long
        self.lat = lat


def isinpolygon(point,vertex_lst, contain_boundary=True):
    #检测点是否位于区域外接矩形内
    lngaxis, lataxis = zip(*vertex_lst)

    minlng, maxlng = min(lngaxis),max(lngaxis)
    minlat, maxlat = min(lataxis),max(lataxis)
    lng, lat = point
    if contain_boundary:
        isin = (minlng<=lng<=maxlng) & (minlat<=lat<=maxlat)
    else:
        isin = (minlng<lng<maxlng) & (minlat<lat<maxlat)
    return isin

def isintersect(poi,spoi,epoi):
    #输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    #射线为向东的纬线
    #可能存在的bug，当区域横跨本初子午线或180度经线的时候可能有问题
    lng, lat = poi
    slng, slat = spoi
    elng, elat = epoi
    if poi == spoi:
        #print("在顶点上")
        return None
    if slat==elat: #排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if slat>lat and elat>lat: #线段在射线上边
        return False
    if slat<lat and elat<lat: #线段在射线下边
        return False
    if slat==lat and elat>lat: #交点为下端点，对应spoint
        return False
    if elat==lat and slat>lat: #交点为下端点，对应epoint
        return False
    if slng<lng and elng<lng: #线段在射线左边
        return False
    #求交点
    xseg=elng-(elng-slng)*(elat-lat)/(elat-slat)
    if xseg == lng:
        #print("点在多边形的边上")
        return None
    if xseg<lng: #交点在射线起点的左侧
        return False
    return True  #排除上述情况之后

def isin_multipolygon(poi,vertex_lst, contain_boundary=True):
    # 判断是否在外包矩形内，如果不在，直接返回false
    if not isinpolygon(poi, vertex_lst, contain_boundary):
        return False
    sinsc = 0
    for spoi, epoi in zip(vertex_lst[:-1],vertex_lst[1::]):
        intersect = isintersect(poi, spoi, epoi)
        if intersect is None:
            return (False, True)[contain_boundary]
        elif intersect:
            sinsc+=1
    return sinsc%2==1

def pintoToPolygonMinDist(long,lat, lk,contain_boundary=True) :
    if not lk:
        lk = "120.854664,30.673868;120.854844,30.671414;120.857898,30.67157;120.85779,30.672129;120.86185,30.672067;120.861814,30.674831;120.860557,30.677844;120.860233,30.680919;120.859407,30.681136;120.858401,30.681105;120.858329,30.681415;120.856353,30.680794;120.856353,30.680515;120.855023,30.679769;120.85664,30.677223;120.854879,30.676042;120.855598,30.675173;120.854808,30.674707;120.854915,30.674085"
    lk1 = lk.split(";")
    points = []
    for x in lk1:
        [x1,x2] = x.split(",")
        points.append([float(x1),float(x2)])

    if not points[-1]==points[0]:
        points.append(points[0])

    isIn = isin_multipolygon([long,lat],points, contain_boundary=True)
    if isIn :
        return -1

    dist = 1.7976931348623157E308

    p = Point(long,lat)
    for i in  range(len(points)-1):
        j = i + 1
        a = Point(points[i][0], points[i][1])
        b = Point(points[j][0], points[j][1])

        dist = min([dist, pointToLineDis(p, a, b)])

    return dist


def pointToLineDis(p, a, b):
    ABx = b.long - a.long
    ABy = b.lat - a.lat

    APx = p.long - a.long
    APy = p.lat - a.lat

    AB_AP = ABx * APx + ABy * APy
    distAB2 = ABx * ABx + ABy * ABy

    Dx = a.long
    Dy = a.lat

    if (distAB2 != 0):
        t = AB_AP / distAB2
        if (t >= 1):
            Dx = b.long
            Dy = b.lat
        elif t > 0:
            Dx = a.long + ABx * t
            Dy = a.lat + ABy * t
        else:
            Dx = a.long
            Dy = a.lat
    juli = LonLatDistance(Dx, Dy, p.long, p.lat)
    return round(juli)

def LonLatDistance(px,py,ax,ay):
    if (px == ax and py == ay) :
      0.0
    else :
        distance = 6378137 * 2 * math.asin(math.sqrt(math.pow(math.sin((py - ay) * math.acos(-1) / 360), 2) +
      math.cos(py * math.acos(-1) / 180) * math.cos(ay * math.acos(-1) / 180) * math.pow(math.sin((px - ax) * math.acos(-1) / 360), 2)))
    return distance

def run(spark):
    spark.sql("drop table if exists tmp_cl_jingqu_grid1_123")
    spark.sql(""" create table tmp_cl_jingqu_grid1_123 as
               select * from (
    select id,grid_lng_cent,grid_lat_cent,grid_id,t2.name,t2.type,ptpmd(cast(grid_lng_cent as double),cast(grid_lat_cent as double),t2.vmap) dis,t1.city_id,t1.city_name,t1.county_name,t1.town_name
from (
 select a.id,a.grid_lng_cent,a.grid_lat_cent,a.grid_id,b.city_id ,b.city_name,b.county_name,b.town_name from dwfu_ns2_hive_db.I_CDM_BD09_GRID a
  join (select * from dwfu_ns2_hive_db.I_CDM_GRID2COMMUNITY where  city_id=3304) b on a.id=b.id
  ) t1  join qs_cssys_jq_ms t2
   ) t3 where dis*1 <=100000
    """)
    # .repartition(10).write.mode("overwrite").saveAsTable("tmp_cl_jingqu_grid")

def main():
    # 初始化spark
    spark = SparkSession.Builder().appName('zz_jingqu').enableHiveSupport().getOrCreate()
    sc = spark.sparkContext
    # 初始化数据库
    spark.sql('use dev_ns2_hive_db')
    # 设置日志级别
    sc.setLogLevel('WARN')
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict ")
    spark.sql("set hive.exec.dynamic.partition=true")
    spark.sql("set hive.exec.compress.output=true")
    spark.sql("set mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec")

    spark.udf.register("ptpmd", pintoToPolygonMinDist)
    run(spark)
    spark.stop()


if __name__ == '__main__':
    main()
