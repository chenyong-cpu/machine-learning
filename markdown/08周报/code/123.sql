create table temp_carbrandname_1_1ji_7_17 as 
select carbrandname,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
      end carbrandname ,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071708,2022071709,
    2022071710)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carbrandname is not null
union all 
select carbrandname,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
      end carbrandname ,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (
      2022071711,2022071712,2022071713
    )
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carbrandname is not null
union all 
select carbrandname,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
      end carbrandname ,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071714,2022071715,
    2022071716)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carbrandname is not null
union all 
select carbrandname,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
      end carbrandname ,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071717,2022071718,2022071719)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carbrandname is not null
union all 
select carbrandname,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
      end carbrandname ,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071720,2022071721,
    2022071722)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carbrandname is not null
union all 
select carbrandname,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChwEoWDylfGAOuKfAAA5bSitpkk273') > 0 then '吉利'
      WHEN instr(uri,'ChsEeV26zOKAATwCAAAMlhPv54M195') > 0 then '大众'
      WHEN instr(uri,'ChwFkl9y_JqAVybMAAAUINDQ2uo180') > 0 then '长安'
      WHEN instr(uri,'ChwEl2D07IOARsLxAAAV_tLtRsA356') > 0 then '长城汽车'
      WHEN instr(uri,'ChwFkmGgkM-ADLF_AAA7SzrQUQw971') > 0 then '丰田'
      WHEN instr(uri,'ChsEe1-WX_yAJ5XBAAAbmbJPOi8696') > 0 then '上汽'
      WHEN instr(uri,'ChsEwGDymG6ATewSAAAMXREb5AQ823') > 0 then '本田'
      WHEN instr(uri,'ChsEf1_llNOAIrJgAAAQANAIBSA602') > 0 then '长安欧尚'
      end carbrandname ,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071723,2022071724)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carbrandname is not null


----------------------2级------------------------
create table temp_carname_1_2ji_7_17 as 
select carname,p_hour,msisdn from (
    select 
    CASE
      WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'   
      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'    
      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
    end carname,p_hour,msisdn
     from  default.d_ens_http_4g where p_hour in (2022071708,2022071709,
    2022071710)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname is not null
union all 
select carname,p_hour,msisdn from (
    select 
    CASE
      WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'   
      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'    
      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
    end carname,p_hour,msisdn
     from  default.d_ens_http_4g where p_hour in (2022071711,2022071712,2022071713)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname is not null
union all 
select carname,p_hour,msisdn from (
    select 
    CASE
      WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'   
      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'    
      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
    end carname,p_hour,msisdn
     from  default.d_ens_http_4g where p_hour in (2022071714,2022071715,
    2022071716)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname is not null
union all 
select carname,p_hour,msisdn from (
    select 
    CASE
      WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'   
      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'    
      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
    end carname,p_hour,msisdn
     from  default.d_ens_http_4g where p_hour in (2022071717,2022071718,2022071719)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname is not null
union all 
select carname,p_hour,msisdn from (
    select 
    CASE
      WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'   
      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'    
      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
    end carname,p_hour,msisdn
     from  default.d_ens_http_4g where p_hour in (2022071720,2022071721,
    2022071722)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname is not null
union all 
select carname,p_hour,msisdn from (
    select 
    CASE
      WHEN  instr(uri,'ChwFlGLHl3qAPWTPAD6WqPvooP8611') > 0  then '星瑞'
      WHEN  instr(uri,'ChxkrmDxNKWALy9BACMXou_Y18k777') > 0  then '星越L'
      WHEN  instr(uri,'ChsEf1yjnlCAVSizAAd1AqfNPIc842') > 0  then '第四代帝豪'
      WHEN  instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0  then '帝豪S'
      WHEN  instr(uri,'ChsE2GEDQd6AdmORABk_yjJVSfI327') > 0  then '缤越'
      WHEN  instr(uri,'Chxkj2FAbHKAHI_nAFZagYHeEew558') > 0  then '远景X6PRO'
      WHEN  instr(uri,'ChwFkWGWGrSAbAldABJqjrZ3cBc349') > 0  then '速腾'
      WHEN  instr(uri,'ChwFkmBxJACAA7T4ABhf6QRm86w922') > 0  then 'UNI-K'
      WHEN  instr(uri,'ChsFJ2J6iv-AVqclAAwwXPoFlzc210') > 0  then '逸动plus'
      WHEN  instr(uri,'wKgH2Vjbb9aAGfbYABBqX4K5vGU861') > 0  then '长安CS35Plus'   
      WHEN  instr(uri,'ChtliGJnb8mAI2NgAIB3_OeC1ss646') > 0  then '哈佛M6'
      WHEN  instr(uri,'ChwFkmAjRW2AY-v1ACLP6OCHYhA442') > 0  then '卡罗拉'
      WHEN  instr(uri,'ChxkmmGND86AHqpcABLrZ-hiML4761') > 0  then '哈佛神兽'
      WHEN  instr(uri,'ChsEdmBxHseADi9wABBLMi6-A9s200') > 0  then '荣威i5'
      WHEN  instr(uri,'Chtk3WC4YhmAF_UcAAeUp_kjTNE700') > 0  then '卡罗拉CROSS'    
      WHEN  instr(uri,'Chxkm2HzY9uAXflFABBgjJnVk-E587') > 0  then '缤智'
      WHEN  instr(uri,'ChwFkWG0iJOAFYtkAAvui_vsSUk612') > 0  then '欧尚X5'
    end carname,p_hour,msisdn
     from  default.d_ens_http_4g where p_hour in (2022071723,2022071724)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname is not null

--------------------------3级----------------------------
create table temp_carname_1_3ji_7_17 as 
select carname2,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
    end carname2,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071708,2022071709,
    2022071710)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname2 is not null
union all
select carname2,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
    end carname2,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071711,2022071712,2022071713)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname2 is not null
union all 
select carname2,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
    end carname2,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071714,2022071715,
    2022071716)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname2 is not null
union all 
select carname2,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
    end carname2,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071717,2022071718,2022071719)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname2 is not null
union all 
select carname2,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
    end carname2,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071720,2022071721,
    2022071722)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname2 is not null
union all 
select carname2,p_hour,msisdn from (
    select 
    CASE
      WHEN instr(uri,'ChtliGJ7MP6AHgYVACFpGtw7pEM506') > 0 then '星瑞'
      WHEN instr(uri,'ChwFj2IdbveATP-xAB6voGWKJdk165') > 0 then '星越L'
      WHEN instr(uri,'ChxkmWK9Em6AK3jBAA9ORFt5puI448') > 0 then '第四代帝豪'
      WHEN instr(uri,'ChxknGJE-fSAY1EcABgv1sq2h7c267') > 0 then '帝豪S'
      WHEN instr(uri,'ChsEoGEZ3ciAUu0wAB0iGvrbcPA477') > 0 then '缤越'
      WHEN instr(uri,'ChxkjmFprtGAG8XQACkPcIS9HQI962') > 0 then '远景X6 PRO'
      WHEN instr(uri,'ChxkmmKWveaAU6rTACLyWlQDOpA183') > 0 then '速腾'
      WHEN instr(uri,'ChwFkGF78YOAFiFNABCLRN1saN4324') > 0 then 'UNI-K'
      WHEN instr(uri,'ChxkqWKVr72AI2-lACAEYq6Yc7s523') > 0 then '逸动plus'
      WHEN instr(uri,'ChtliGKHKRyAQuTvABqx_84lEDg350') > 0 then '长安CS35 PLUS'
      WHEN instr(uri,'ChsEmF_kZ1SAc6rmADTADD8C70Y653') > 0 then '哈佛M6'
      WHEN instr(uri,'ChsFVWKK852AB9UPADhrkLRlVJE825') > 0 then '卡罗拉'
      WHEN instr(uri,'ChwFkmGPrgqAJGkMACx41qsEpZs250') > 0 then '哈佛神兽'
      WHEN instr(uri,'ChwEmGCKeeuAYUb_ADD9mFBpGn4820') > 0 then '荣威i5'
      WHEN instr(uri,'ChwFlV-Pq1WAcl4rACDB9j24L8A760') > 0 then '缤智'
      WHEN instr(uri,'ChwFkWGefNqAVLmzACPPbSlxuP8585') > 0 then '欧尚X50'
    end carname2,p_hour, msisdn
    from  default.d_ens_http_4g where p_hour in (2022071723,2022071724)
    and HOST in ('car3.autoimg.cn','car2.autoimg.cn')
    and substr(msisdn,1,1)='1' 
    and substr(msisdn,1,3)<>'106' 
    and substr(msisdn,1,3)<>'144' 
    and substr(msisdn,1,2)<> '12' 
    and msisdn not rlike '[a-zA-Z]'
) where carname2 is not null