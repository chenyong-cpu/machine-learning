package 意向购车模型.调
import org.apache.spark.sql.types.{StringType, StructField, StructType}
import org.apache.spark.sql.{DataFrame, Row, SaveMode, SparkSession}
import org.apache.spark.{SparkConf, SparkContext}

import scala.collection.mutable.ArrayBuffer
import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel
import org.slf4j.{Logger, LoggerFactory}

object SparkJob {

  private val ESP: Double = 1e-5
  private val INFINITY: Double = 1e10

  val logger: Logger = LoggerFactory.getLogger(SparkJob.getClass)

  def main(args: Array[String]): Unit = {

    val time: Long = System.currentTimeMillis()

    // 初始化sparksession
    val spark: SparkSession = SparkSession.builder().appName("model_access_tool"+ time)
      .config("spark.sql.shuffle.partitions",400)
      .config("spark.sql.crossJoin.enabled",true)
      .enableHiveSupport().getOrCreate()
    // 使用数据库
    spark.sql("use bdcqs_hive_db")
    spark.sql("set hive.merge.mapfiles=true")
    spark.sql("set hive.merge.mapredfiles=true")
    spark.sql("set hive.exec.compress.output=true")
    spark.sql("set hive.merge.size.per.task = 1073741824")
    spark.sql("set hive.merge.smallfiles.avgsize=1073741824")
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict")
    spark.sql("set spark.hadoop.hive.exec.orc.split.strategy=ETL")
    spark.sql("set mapreduce.input.fileinputformat.split.minsize=1")
    spark.sql("set mapreduce.input.fileinputformat.split.maxsize=1073741824")
    spark.sql("set mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec")

    //获取目标栅格的数据
    spark.sql(
      s"""
         |select uri,p_hour,msisdn
         |    from  default.d_ens_http_4g where p_hour in (${yyyyMMdd}01,${yyyyMMdd}02,${yyyyMMdd}03,${yyyyMMdd}04,${yyyyMMdd}05,${yyyyMMdd}06)
         |    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
         |    and msisdn>10000000000 and msisdn<20000000000
       """.stripMargin).repartition(60).write.mode(SaveMode.Overwrite).saveAsTable("temp_szh_carbrandname_1")
    spark.sql(
      s"""
         |select uri,p_hour,msisdn
         |    from  default.d_ens_http_4g where p_hour in (${yyyyMMdd}07,${yyyyMMdd}08,${yyyyMMdd}09,${yyyyMMdd}10,${yyyyMMdd}11,${yyyyMMdd}12)
         |    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
         |    and msisdn>10000000000 and msisdn<20000000000
       """.stripMargin).repartition(60).write.mode(SaveMode.Append).saveAsTable("temp_szh_carbrandname_1")

    spark.sql(
      s"""
         |select uri,p_hour,msisdn
         |    from  default.d_ens_http_4g where p_hour in (${yyyyMMdd}13,${yyyyMMdd}14,${yyyyMMdd}15,${yyyyMMdd}16,${yyyyMMdd}17,${yyyyMMdd}18)
         |    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
         |    and msisdn>10000000000 and msisdn<20000000000
       """.stripMargin).repartition(60).write.mode(SaveMode.Append).saveAsTable("temp_szh_carbrandname_1")

    spark.sql(
      s"""
         |select uri,p_hour,msisdn
         |    from  default.d_ens_http_4g where p_hour in (${yyyyMMdd}19,${yyyyMMdd}20,${yyyyMMdd}21,${yyyyMMdd}22,${yyyyMMdd}23)
         |    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
         |    and msisdn>10000000000 and msisdn<20000000000
       """.stripMargin).repartition(60).write.mode(SaveMode.Append).saveAsTable("temp_szh_carbrandname_1")

    spark.sql(
      s"""
         |select CASE WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
         |      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
         |      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
         |      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
         |      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
         |      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
         |      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
         |      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
         |      end carbrandname
         |      ,CASE WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
         |      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
         |      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
         |      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
         |      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
         |      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
         |      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
         |      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
         |      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
         |      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'
         |      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
         |      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
         |      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
         |      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
         |      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'
         |      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
         |      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
         |    end carname
         |    ,CASE WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
         |      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
         |      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
         |      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
         |      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
         |      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
         |      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
         |      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
         |      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
         |      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
         |      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
         |      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
         |      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
         |      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
         |      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
         |      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
         |    end carname2
         |      ,p_hour,msisdn
         |    from  temp_szh_carbrandname_1
         |    where (uri regexp 'ChwEoWDylfGAOuKfAAA5bSitpkk273|ChsEeV26zOKAATwCAAAMlhPv54M195|ChwFkl9y_JqAVybMAAAUINDQ2uo180|ChwEl2D07IOARsLxAAAV_tLtRsA356|ChwFkmGgkM-ADLF_AAA7SzrQUQw971|ChsEe1-WX_yAJ5XBAAAbmbJPOi8696|ChsEwGDymG6ATewSAAAMXREb5AQ823|ChsEf1_llNOAIrJgAAAQANAIBSA602'
         |    or uri regexp 'ChwFlGLHl3qAPWTPAD6WqPvooP8611|ChxkrmDxNKWALy9BACMXou_Y18k777|ChsEf1yjnlCAVSizAAd1AqfNPIc842|ChxknGJE-fSAY1EcABgv1sq2h7c267|ChsE2GEDQd6AdmORABk_yjJVSfI327|Chxkj2FAbHKAHI_nAFZagYHeEew558|ChwFkWGWGrSAbAldABJqjrZ3cBc349|ChwFkmBxJACAA7T4ABhf6QRm86w922|ChsFJ2J6iv-AVqclAAwwXPoFlzc210|wKgH2Vjbb9aAGfbYABBqX4K5vGU861|ChtliGJnb8mAI2NgAIB3_OeC1ss646|ChwFkmAjRW2AY-v1ACLP6OCHYhA442|ChxkmmGND86AHqpcABLrZ-hiML4761|ChsEdmBxHseADi9wABBLMi6-A9s200|Chtk3WC4YhmAF_UcAAeUp_kjTNE700|Chxkm2HzY9uAXflFABBgjJnVk-E587|ChwFkWG0iJOAFYtkAAvui_vsSUk612'
         |    or uri regexp 'ChtliGJ7MP6AHgYVACFpGtw7pEM506|ChwFj2IdbveATP-xAB6voGWKJdk165|ChxkmWK9Em6AK3jBAA9ORFt5puI448|ChxknGJE-fSAY1EcABgv1sq2h7c267|ChsEoGEZ3ciAUu0wAB0iGvrbcPA477|ChxkjmFprtGAG8XQACkPcIS9HQI962|ChxkmmKWveaAU6rTACLyWlQDOpA183|ChwFkGF78YOAFiFNABCLRN1saN4324|ChxkqWKVr72AI2-lACAEYq6Yc7s523|ChtliGKHKRyAQuTvABqx_84lEDg350|ChsEmF_kZ1SAc6rmADTADD8C70Y653|ChsFVWKK852AB9UPADhrkLRlVJE825|ChwFkmGPrgqAJGkMACx41qsEpZs250|ChwEmGCKeeuAYUb_ADD9mFBpGn4820|ChwFlV-Pq1WAcl4rACDB9j24L8A760|ChwFkWGefNqAVLmzACPPbSlxuP8585')
       """.stripMargin).repartition(60).write.mode(SaveMode.Overwrite).saveAsTable("temp_szh_carbrandname_2")

    spark.sql(
      s"""
         |insert overwrite table L_4S_HTTP_CARBRANDNAME_D partition (P_DAY,P_HOUR)
         |select
         |CARBRANDNAME
         |,CARNAME
         |,CARNAME2
         |,msisdn as PHONE
         |,P_HOUR
         |,substr(P_HOUR,1,8) as P_DAY
         |from temp_szh_carbrandname_2
       """.stripMargin)
    //    var a=spark.sql(
    //      s"""
    //         |select mon_time_one,date_format(date_sub(from_unixtime(unix_timestamp(mon_time_one,'yyyyMM'),'yyyy-MM-dd'),1),'yyyyMMdd') day_time_one
    //         |,mon_time_two,date_format(date_sub(from_unixtime(unix_timestamp(mon_time_two,'yyyyMM'),'yyyy-MM-dd'),1),'yyyyMMdd') day_time_two
    //         |from
    //         |(select date_format(add_months(from_unixtime(unix_timestamp('${yyyyMM}','yyyyMM'),'yyyy-MM-dd'),-1),'yyyyMM') mon_time_one
    //         |,date_format(add_months(from_unixtime(unix_timestamp('${yyyyMM}','yyyyMM'),'yyyy-MM-dd'),-2),'yyyyMM') mon_time_two)a
    //      """.stripMargin).rdd.collect()
    spark.sql(
      s"""
         |drop table temp_szh_carbrandname_2
       """.stripMargin)
    spark.sql(
      s"""
         |drop table temp_szh_carbrandname_1
       """.stripMargin)
    spark.close()

  }

}



