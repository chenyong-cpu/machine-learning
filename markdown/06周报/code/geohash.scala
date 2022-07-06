import org.apache.spark.sql.types.{StringType, StructField, StructType}
import org.apache.spark.sql.{DataFrame, Row, SaveMode, SparkSession}
import org.apache.spark.{SparkConf, SparkContext}

import scala.collection.mutable.ArrayBuffer
import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel
import org.slf4j.{Logger, LoggerFactory}

import org.apache.spark.sql.SparkSession

object SparkJob {

  def intercalate[A](a: List[A], b: List[A]): List[A] = a match {
    case h :: t => h :: intercalate(b, t)
    case _      => b
  }

  val BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"
  val BITS = Array(16, 8, 4, 2, 1) // scalastyle:ignore
  val TODEC = Map(BASE32.zipWithIndex: _*)

  def toBase32(bin: Seq[Boolean]): Char = BASE32((BITS zip bin).collect { case (x, true) => x }.sum)

  val LAT_RANGE = (-90.0, 90.0)
  val LON_RANGE = (-180.0, 180.0)

  // Aliases, utility functions
  type Bounds = (Double, Double)
  private def mid(b: Bounds) = (b._1 + b._2) / 2.0
  implicit class BoundedNum(x: Double) { def in(b: Bounds): Boolean = x >= b._1 && x <= b._2 }

  /**
   * togeohash lat/long as a base32 geohash.
   *
   * Precision (optional) is the number of base32 chars desired; default is 12, which gives precision well under a meter.
   */
  def togeohash(lat: Double, lon: Double, precision: Int=12): String = { // scalastyle:ignore
    require(lat in LAT_RANGE, "Latitude out of range")
    require(lon in LON_RANGE, "Longitude out of range")
    require(precision > 0, "Precision must be a positive integer")
    val rem = precision % 2 // if precision is odd, we need an extra bit so the total bits divide by 5
    val numbits = (precision * 5) / 2
    val latBits = findBits(lat, LAT_RANGE, numbits)
    val lonBits = findBits(lon, LON_RANGE, numbits + rem)
    val bits = intercalate(lonBits, latBits)
    bits.grouped(5).map(toBase32).mkString // scalastyle:ignore
  }

  private def findBits(part: Double, bounds: Bounds, p: Int): List[Boolean] = {
    if (p == 0) Nil
    else {
      val avg = mid(bounds)
      if (part >= avg) true :: findBits(part, (avg, bounds._2), p - 1) // >= to match geohash.org encoding
      else false :: findBits(part, (bounds._1, avg), p - 1)
    }
  }

  def main(args: Array[String]): Unit = {
    val time: Long = System.currentTimeMillis()
    val spark: SparkSession = SparkSession.builder().appName("model_access_tool"+ time)
      .config("spark.sql.shuffle.partitions",400)
      .config("spark.sql.crossJoin.enabled",true)
      .enableHiveSupport().getOrCreate()

    spark.sql("use bdcqs_hive_db")
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict ")
    spark.sql("set hive.exec.dynamic.partition=true")
    spark.sql("set hive.exec.compress.output=true")
    spark.sql("set mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec")
    spark.sql("set spark.hadoop.hive.exec.orc.split.strategy=ETL")

    import spark.implicits._
    //清空结果表
    spark.sql(
      """
        |drop table if exists qm_sm_users_all
      """.stripMargin)

    spark.sql(
      """
        |drop table if exists qm_sm_users
      """.stripMargin)

    spark.sql(
      """
        |drop table if exists qm_sm_poi
      """.stripMargin)

    spark.sql(
      """
        |drop table if exists qm_sm_test1
      """.stripMargin)

    spark.sql(
      """
        |drop table if exists qm_sm_test
      """.stripMargin)


    spark.udf.register("togeohash",togeohash(_:Double,_:Double,_:Int))


    //筛选公墓基站 所有用户
    spark.sql(
      """
        |select
        |      a.p_day,a.bill_no,a.lac_ci,b.SITE_NAME,a.in_time,a.end_time,a.STAY_DURATION,b.LONGITUDE,b.LATITUDE
        |              from dwfu_hive_db.I_TPOS_TRAIL_COUNTRY_D a
        |              join dwfu_hive_db.I_CDM_LACCI_ZJ b
        |              on a.lac_ci = b.lac_ci
        |              where a.p_day='20220322'
        |               and substr(a.bill_no,1,1)=1
		|               and substr(a.bill_no,1,2) >'12'
		|               and length(a.bill_no)=11
		|               and substr(a.bill_no,1,3) not in ('106','144')
        |               and a.STAY_DURATION>1800
        |               and b.COVER_AREA = '公墓'
        |""".stripMargin).repartition(20).write.mode(SaveMode.Overwrite).saveAsTable("qm_sm_users_all")
    //剔除常驻用户
    spark.sql(
      """
        |select a.p_day,a.bill_no,a.lac_ci,a.SITE_NAME,a.in_time,a.end_time,a.STAY_DURATION,a.LONGITUDE,a.LATITUDE,togeohash(cast(a.LATITUDE as double),cast(a.LONGITUDE as double),5) as grid_id from
        |      qm_sm_users_all a
        |       left join
        |       (
        |         select t1.p_day,t1.bill_no from
        |         		(
        |                 select p_day,bill_no,STAY_LAC_CI,STAY_DAYS
        |                  		from dwfu_hive_db.A_TPOS_STAY_PRODUCT_D
        |                        where p_day = '20220322'
        |                        and STAY_DAYS > 15
        |                ) t1
        |                join DWFU_HIVE_DB.I_CDM_LACCI_ZJ t2
        |                on t1.STAY_LAC_CI = t2.lac_ci
        |
        |         		where t2.COVER_AREA = '公墓'
        |      ) b
        |      on a.bill_no = b.bill_no and a.p_day=b.p_day
        |      where b.bill_no is null
        |""".stripMargin).repartition(20).write.mode(SaveMode.Overwrite).saveAsTable("qm_sm_users")
    //公墓poi表
    spark.sql(
      """
        |select p_day,poi_id,city_name,grid_id ,poi_name from (
        |select p_day,poi_id,regexp_replace(city_name,'市','') as city_name,togeohash(cast(GRID_CENT_LAT as double),cast(GRID_CENT_LNG as double),5) as grid_id ,poi_name,
        |   row_number() over(partition by p_day,GRID_CENT_LAT,GRID_CENT_LNG,regexp_replace(city_name,'市','') order by poi_id ) as rn
        |     from dwfu_hive_db.I_UPOS_POI_D
        |      where p_day='20220322'
        |       and PROV_NAME='浙江省'
        |       and (POI_ORIGIN_CLS like '%丧葬%'
        |               or POI_ORIGIN_CLS like '%殡葬%'
        |               or POI_ORIGIN_CLS like '%公墓%'
        |               or POI_ORIGIN_CLS like '%陵园%'
        |               or poi_name rlike'公墓'
        |           )
        |      )
        |      where rn=1
        |""".stripMargin).repartition(20).write.mode(SaveMode.Overwrite).saveAsTable("qm_sm_poi")
    spark.sql(
      """
        |    select t1.p_day,t1.bill_no,t1.lac_ci,t1.in_time,t1.end_time,t1.STAY_DURATION as stay_time,nvl(t2.poi_name,t1.SITE_NAME) as cemetery_name,t2.poi_id,t2.city_name from
        |    qm_sm_users t1
        |    left join
        |     qm_sm_poi t2
        |      on t1.p_day=t2.p_day and t1.grid_id=t2.grid_id
        |""".stripMargin).repartition(20).write.mode(SaveMode.Overwrite).saveAsTable("qm_sm_test1")

    spark.sql(
      """
        |    select  p_day,bill_no,lac_ci,in_time,end_time,stay_time,cemetery_name,poi_id,city_name from (
        |       select  p_day,bill_no,lac_ci,in_time,end_time,stay_time,cemetery_name,poi_id,city_name,
        |       row_number() over(partition by p_day,bill_no,lac_ci,in_time,end_time,stay_time,city_name order by poi_id ) as rn
        |       from qm_sm_test1
        |       )
        |     where rn=1
        |""".stripMargin).repartition(20).write.mode(SaveMode.Overwrite).saveAsTable("qm_sm_test")

    spark.close()
  }

}


