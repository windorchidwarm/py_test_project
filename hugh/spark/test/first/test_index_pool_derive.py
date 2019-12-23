import time
from pyspark.sql import SparkSession


def log(index="", sql="", rs=""):
    print("==============================start  指标：{}=======================================".format(index))
    print(sql)
    print("==============================end  指标：{}=======================================".format(index))


warehouseLocation = "hdfs:///user/hive/warehouse"
spark = SparkSession \
    .builder \
    .appName("index_fetch1") \
    .config("spark.sql.warehouse.dir", warehouseLocation) \
    .enableHiveSupport() \
    .getOrCreate()

#############通用变量############################
common_dt = '20190902'
dishonest_dt = '20190502'
offline_relation_dt = '20190819'
current_date = '2019-10-01'
before_dot_5_year = '2019-04-01'
before_1_year = '2018-10-01'
before_2_year = '2017-10-01'
before_3_year = '2016-10-01'
before_5_year = '2014-10-01'

######################目标企业##########################
sample_id = spark.read.csv('/user/dptest/ids', header=True, sep=',')
sample_id.createOrReplaceTempView('sample_id')

######################公共数据提取#################################
df_degree1 = spark.sql('''
        select bbd_qyxx_id,source_bbd_id as id from dw.off_line_relations where dt='{}' and source_degree=1 and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
        union distinct 
        select bbd_qyxx_id,destination_bbd_id  as id from dw.off_line_relations where dt='{}' and destination_degree=1 and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
'''.format(offline_relation_dt, offline_relation_dt))
df_degree1.createOrReplaceTempView('degree1')

df_degree2 = spark.sql('''
        select bbd_qyxx_id,source_bbd_id as id from dw.off_line_relations where dt='{}' and source_degree=2 and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
        union distinct 
        select bbd_qyxx_id,destination_bbd_id  as id from dw.off_line_relations where dt='{}' and destination_degree=2 and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
'''.format(offline_relation_dt, offline_relation_dt))
df_degree1.createOrReplaceTempView('degree2')
######################## 10Y,qy_jyzt,企业经营状态##############################################
# 目标企业的经营状态	[dw.qyxx_basic](bbd_qyxx_id, company_enterprise_status)

sql_10Y = '''
                SELECT
                    bbd_qyxx_id,
                    company_enterprise_status as index_10Y
                FROM
                    dw.qyxx_basic 
                WHERE
                    dt = '{}' 
                    AND bbd_qyxx_id IN ( select bbd_qyxx_id from sample_id  ) 
                ORDER BY bbd_qyxx_id
'''.format(common_dt)

log("10Y", sql_10Y)
df_10Y = spark.sql(sql_10Y)

######################## 4B,qy_jynx_num,企业经营年限##############################################

sql_4B = '''
   select bbd_qyxx_id,bround(months_between(to_date('{}','yyyyMMdd'),esdate)/12,0) as index_4B from dw.qyxx_basic where dt='{}' and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
'''.format(common_dt, common_dt, common_dt)
log("4B", sql_4B)
df_4B = spark.sql(sql_4B)

######################## 14Y	qy_hy	企业行业##############################################

sql_14Y = '''
   select bbd_qyxx_id, company_industry as index_14Y from dw.qyxx_basic where dt='{}'   and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
'''.format(common_dt)
log("14Y", sql_14Y)
df_14Y = spark.sql(sql_14Y)

######################## 11Y	qy_dq	企业地区##############################################

sql_11Y = '''
   select bbd_qyxx_id, company_county as index_11Y from dw.qyxx_basic where dt='{}'   and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
'''.format(common_dt)
log("11Y", sql_11Y)
df_11Y = spark.sql(sql_11Y)

######################## 2Y	qy_ssgs_is	企业上市公司与否##############################################

sql_2Y = '''
   select distinct bbd_qyxx_id,1 as index_2Y from dw.qyxg_jqka_ipo_basic where dt='{}'   and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
'''.format(common_dt)
log("2Y", sql_2Y)
df_2Y = spark.sql(sql_2Y)

######################## 368C	qy_jdktgg_num_1year	企业借贷相关开庭公告数量近一年#############################

sql_368C = '''
   select bbd_qyxx_id,count(distinct case_code) as index_368C from dw.ktgg where dt='{}' 
and 
(
regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or 
regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or
regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
)
and
trial_date>=to_date('{}')
and 
trial_date < to_date('{}')
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("368C", sql_368C)
df_368C = spark.sql(sql_368C)

######################## 369C	qy_jdktgg_num_3year	企业借贷相关开庭公告数量近三年#############################

sql_369C = '''
   select bbd_qyxx_id,count(distinct case_code) as index_369C from dw.ktgg where dt='{}' 
and 
(
regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or 
regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or
regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
)
and
trial_date>=to_date('{}')
and 
trial_date < to_date('{}')
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("369C", sql_369C)
df_369C = spark.sql(sql_369C)

######################## 370C	qy_jdktgg_num_5year	企业借贷相关开庭公告数量近五年#############################

sql_370C = '''
   select bbd_qyxx_id,count(distinct case_code) as index_370C from dw.ktgg where dt='{}' 
and 
(
regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or 
regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or
regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
)
and
trial_date>=to_date('{}')
and 
trial_date < to_date('{}')
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("370C", sql_370C)
df_370C = spark.sql(sql_370C)

######################## 371C	qy_jdcpws_num_1year	企业借贷相关裁判文书数据近一年#############################

sql_371C = '''
select bbd_qyxx_id,count(*) as index_371C from dw.legal_adjudicative_documents where dt='{}'  and 
sentence_date>=to_date('{}')
and
sentence_date<to_date('{}')
and 
(
regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or 
regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or
regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
)
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id
'''.format(common_dt, before_1_year, current_date)
log("371C", sql_371C)
df_371C = spark.sql(sql_371C)

######################## 372C	qy_jdcpws_num_3year	企业借贷相关裁判文书数据近三年#############################

sql_372C = '''
select bbd_qyxx_id,count(*) as index_372C from dw.legal_adjudicative_documents where dt='{}'  and 
sentence_date>=to_date('{}')
and
sentence_date<to_date('{}')
and 
(
regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or 
regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or
regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
)
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("372C", sql_372C)
df_372C = spark.sql(sql_372C)

######################## 373C	qy_jdcpws_num_5year	企业借贷相关裁判文书数据近五年#############################

sql_373C = '''
select bbd_qyxx_id,count(*) as index_373C from dw.legal_adjudicative_documents where dt='{}'  and 
sentence_date>=to_date('{}')
and
sentence_date<to_date('{}')
and 
(
regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or 
regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
or
regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
)
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("373C", sql_373C)
df_373C = spark.sql(sql_373C)

######################## 441C	qy_sx_num	企业失信数量#############################

sql_441C = '''
select bbd_qyxx_id,count(distinct exe_code) as index_441C from dw.dishonesty 
where dt='{}' 
and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
group by bbd_qyxx_id
'''.format(dishonest_dt)
log("441C", sql_441C)
df_441C = spark.sql(sql_441C)

######################## 22C	qy_bzx_num_1year	企业被执行数量近一年#############################
sql_22C = '''
    select bbd_qyxx_id,count(distinct  case_code) as index_22C from dw.legal_persons_subject_to_enforcement
    where dt='{}' 
    and register_date>=to_date('{}') 
    and register_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("22C", sql_22C)
df_22C = spark.sql(sql_22C)

######################## 374C	qy_bzx_num_3year	企业被执行数量近三年#############################
sql_374C = '''
    select bbd_qyxx_id,count(distinct  case_code) as index_374C from dw.legal_persons_subject_to_enforcement
    where dt='{}' 
    and register_date>=to_date('{}') 
    and register_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("374C", sql_374C)
df_374C = spark.sql(sql_374C)

########################375C	qy_bzx_num_5year	企业被执行数量近五年#############################
sql_375C = '''
    select bbd_qyxx_id,count(distinct  case_code) as index_375C from dw.legal_persons_subject_to_enforcement
    where dt='{}' 
    and register_date>=to_date('{}') 
    and register_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("375C", sql_375C)
df_375C = spark.sql(sql_375C)

########################376C	qy_xzcfFJYCX_num_1year	企业行政处罚非简易程序数量近一年#############################
sql_376C = '''
    select bbd_qyxx_id,count(*) as index_376C from dw.xzcf where dt='{}' 
    and regexp_extract(punish_content,'(警告|通报)',1)=''
    and regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) not in('','.')
    and (
    (cast(regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) as DOUBLE) >=1000 ) 
    or 
    (cast(regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) as DOUBLE) >=1 
    and regexp_extract(punish_content,'(千)',1)!=''))
    and
    public_date>=to_date('{}')
    and
    public_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("376C", sql_376C)
df_376C = spark.sql(sql_376C)

########################377C	qy_xzcfFJYCX_num_3year	企业行政处罚非简易程序数量近三年#############################
sql_377C = '''
    select bbd_qyxx_id,count(*) as index_377C from dw.xzcf where dt='{}' 
    and regexp_extract(punish_content,'(警告|通报)',1)=''
    and regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) not in('','.')
    and (
    (cast(regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) as DOUBLE) >=1000 ) 
    or 
    (cast(regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) as DOUBLE) >=1 
    and regexp_extract(punish_content,'(千)',1)!=''))
    and
    public_date>=to_date('{}')
    and
    public_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("377C", sql_377C)
df_377C = spark.sql(sql_377C)

########################378C	qy_xzcfFJYCX_num_5year	企业行政处罚非简易程序数量近五年#############################
sql_378C = '''
    select bbd_qyxx_id,count(*) as index_378C from dw.xzcf where dt='{}' 
    and regexp_extract(punish_content,'(警告|通报)',1)=''
    and regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) not in('','.')
    and (
    (cast(regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) as DOUBLE) >=1000 ) 
    or 
    (cast(regexp_extract(punish_content,'([0-9]+\.?[0-9]*)',1) as DOUBLE) >=1 
    and regexp_extract(punish_content,'(千)',1)!=''))
    and
    public_date>=to_date('{}')
    and
    public_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("378C", sql_378C)
df_378C = spark.sql(sql_378C)

########################382C	qy_fddbrbg_num_6month	企业法定代表人变更数量近六个月#############################
sql_382C = '''
  select bbd_qyxx_id,count(*) as index_382C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='frname'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_dot_5_year, current_date)
log("382C", sql_382C)
df_382C = spark.sql(sql_382C)

########################383C	qy_fddbrbg_num_2year	企业法定代表人变更数量近两年#############################
sql_383C = '''
  select bbd_qyxx_id,count(*) as index_383C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='frname'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_2_year, current_date)
log("383C", sql_383C)
df_383C = spark.sql(sql_383C)

########################123C	qy_jyfwbg_num_1year	企业经营范围变更数量近一年#############################
sql_123C = '''
  select bbd_qyxx_id,count(*) as index_123C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='operate_scope'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("123C", sql_123C)
df_123C = spark.sql(sql_123C)

########################384C	qy_jyfwbg_num_3year	企业经营范围变更数量近三年#############################
sql_384C = '''
  select bbd_qyxx_id,count(*) as index_384C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='operate_scope'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("384C", sql_384C)
df_384C = spark.sql(sql_384C)

########################385C	qy_jyfwbg_num_5year	企业经营范围变更数量近五年#############################
sql_385C = '''
  select bbd_qyxx_id,count(*) as index_385C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='operate_scope'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("385C", sql_385C)
df_385C = spark.sql(sql_385C)

########################113C	qy_jydzbg_num_1year	企业经营地址变更数量近一年	#############################
sql_113C = '''
  select bbd_qyxx_id,count(*) as index_113C from dw.qyxx_bgxx_merge_clean 
    where dt='{}' 
    and change_key='address'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("113C", sql_113C)
df_113C = spark.sql(sql_113C)

########################386C	qy_jydzbg_num_3year	企业经营地址变更数量近三年#############################
sql_386C = '''
  select bbd_qyxx_id,count(*) as index_386C from dw.qyxx_bgxx_merge_clean 
    where dt='{}' 
    and change_key='address'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("386C", sql_386C)
df_386C = spark.sql(sql_386C)

########################387C	qy_jydzbg_num_5year	企业经营地址变更数量近五年#############################
sql_387C = '''
  select bbd_qyxx_id,count(*) as index_387C from dw.qyxx_bgxx_merge_clean 
    where dt='{}' 
    and change_key='address'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("387C", sql_387C)
df_387C = spark.sql(sql_387C)

########################110C	qy_gqdj_num	企业股权冻结数量#############################
sql_110C = '''
    select bbd_qyxx_id,count(distinct frodocno) as index_110C from dw.qyxx_sharesfrost where dt='{}' 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt)
log("110C", sql_110C)
df_110C = spark.sql(sql_110C)

########################440C	qy_gqcz_num	企业股权出质数量############################
sql_440C = '''
    select bbd_qyxx_id,count(distinct morregcno) as index_440C from dw.qyxx_sharesimpawn where dt='{}' 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt)
log("440C", sql_440C)
df_440C = spark.sql(sql_440C)

########################104C	qy_gqbg_num_1year	企业股权变更数量近一年#############################
sql_104C = '''
  select bbd_qyxx_id,count(*) as index_104C from dw.qyxx_bgxx_merge_clean 
    where dt='{}' 
    and change_key='gdxx'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("104C", sql_104C)
df_104C = spark.sql(sql_104C)

########################388C	qy_gqbg_num_3year	企业股权变更数量近三年#############################
sql_388C = '''
  select bbd_qyxx_id,count(*) as index_388C from dw.qyxx_bgxx_merge_clean 
    where dt='{}' 
    and change_key='gdxx'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("388C", sql_388C)
df_388C = spark.sql(sql_388C)

########################389C	qy_gqbg_num_5year	企业股权变更数量近五年#############################
sql_389C = '''
  select bbd_qyxx_id,count(*) as index_389C from dw.qyxx_bgxx_merge_clean 
    where dt='{}' 
    and change_key='gdxx'
    and change_date>=to_date('{}') 
    and change_date<to_date('{}') 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("389C", sql_389C)
df_389C = spark.sql(sql_389C)

########################282C	qy_zczbbgzj_num_1year	企业注册资本变更增加数量近一年#############################
sql_282C = '''
    select bbd_qyxx_id,count(*) as index_282C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='regcap' 
    and regexp_extract(content_after_change,'(\d*\.?\d*)',1)!='' 
    and regexp_extract(content_before_change,'(\d*\.?\d*)',1)!='' 
    and cast(regexp_extract(content_after_change,'(\d*\.?\d*)',1) as double) - cast(regexp_extract(content_before_change,'(\d*\.?\d*)',1) as double) >0
    and
    change_date>=to_date('{}')
    and
    change_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("282C", sql_282C)
df_282C = spark.sql(sql_282C)

########################390C	qy_zczbbgzj_num_3year	企业注册资本变更增加数量近三年#############################
sql_390C = '''
    select bbd_qyxx_id,count(*) as index_390C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='regcap' 
    and regexp_extract(content_after_change,'(\d*\.?\d*)',1)!='' 
    and regexp_extract(content_before_change,'(\d*\.?\d*)',1)!='' 
    and cast(regexp_extract(content_after_change,'(\d*\.?\d*)',1) as double) - cast(regexp_extract(content_before_change,'(\d*\.?\d*)',1) as double) >0
    and
    change_date>=to_date('{}')
    and
    change_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("390C", sql_390C)
df_390C = spark.sql(sql_390C)

########################391C	qy_zczbbgzj_num_5year	企业注册资本变更增加数量近五年#############################
sql_391C = '''
  select bbd_qyxx_id,count(*) as index_391C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='regcap' 
    and regexp_extract(content_after_change,'(\d*\.?\d*)',1)!='' 
    and regexp_extract(content_before_change,'(\d*\.?\d*)',1)!='' 
    and cast(regexp_extract(content_after_change,'(\d*\.?\d*)',1) as double) - cast(regexp_extract(content_before_change,'(\d*\.?\d*)',1) as double) >0
    and
    change_date>=to_date('{}')
    and
    change_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("391C", sql_391C)
df_391C = spark.sql(sql_391C)

########################270C	qy_zczbbgjs_num_1year	企业注册资本变更减少数量近一年#############################
sql_270C = '''
  select bbd_qyxx_id,count(*) as index_270C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='regcap' 
    and regexp_extract(content_after_change,'(\d*\.?\d*)',1)!='' 
    and regexp_extract(content_before_change,'(\d*\.?\d*)',1)!='' 
    and cast(regexp_extract(content_after_change,'(\d*\.?\d*)',1) as double) - cast(regexp_extract(content_before_change,'(\d*\.?\d*)',1) as double) <0
    and
    change_date>=to_date('{}')
    and
    change_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("270C", sql_270C)
df_270C = spark.sql(sql_270C)

########################392C	qy_zczbbgjs_num_3year	企业注册资本变更减少数量近三年#############################
sql_392C = '''
  select bbd_qyxx_id,count(*) as index_392C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='regcap' 
    and regexp_extract(content_after_change,'(\d*\.?\d*)',1)!='' 
    and regexp_extract(content_before_change,'(\d*\.?\d*)',1)!='' 
    and cast(regexp_extract(content_after_change,'(\d*\.?\d*)',1) as double) - cast(regexp_extract(content_before_change,'(\d*\.?\d*)',1) as double) <0
    and
    change_date>=to_date('{}')
    and
    change_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("392C", sql_392C)
df_392C = spark.sql(sql_392C)

########################393C	qy_zczbbgjs_num_5year	企业注册资本变更减少数量近五年#############################
sql_393C = '''
  select bbd_qyxx_id,count(*) as index_393C from dw.qyxx_bgxx_merge_clean where dt='{}' 
    and change_key='regcap' 
    and regexp_extract(content_after_change,'(\d*\.?\d*)',1)!='' 
    and regexp_extract(content_before_change,'(\d*\.?\d*)',1)!='' 
    and cast(regexp_extract(content_after_change,'(\d*\.?\d*)',1) as double) - cast(regexp_extract(content_before_change,'(\d*\.?\d*)',1) as double) <0
    and
    change_date>=to_date('{}')
    and
    change_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("393C", sql_393C)
df_393C = spark.sql(sql_393C)

########################432C	qy_zprs_num_1year	企业招聘人数数量近一年#############################
sql_432C = '''
    select bbd_qyxx_id,sum(bbd_recruit_num) as index_432C from dw.recruit where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("432C", sql_432C)
df_432C = spark.sql(sql_432C)

########################433C	qy_zprs_num_3year	企业招聘人数数量近三年#############################
sql_433C = '''
    select bbd_qyxx_id,sum(bbd_recruit_num) as index_433C from dw.recruit where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("433C", sql_433C)
df_433C = spark.sql(sql_433C)

########################434C	qy_zprs_num_5year	企业招聘人数数量近五年#############################
sql_434C = '''
    select bbd_qyxx_id,sum(bbd_recruit_num) as index_434C from dw.recruit where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("434C", sql_434C)
df_434C = spark.sql(sql_434C)

########################296C	qy_zl_num_1year	企业专利数量近一年#############################
sql_296C = '''
    select bbd_qyxx_id,count(distinct public_code) as index_296C from dw.qyxx_wanfang_zhuanli where dt='{}' 
    and publidate>=to_date('{}')
    and publidate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("296C", sql_296C)
df_296C = spark.sql(sql_296C)

########################379C	qy_jyycYZCD_num_1year	企业经营异常数量严重程度近一年#############################
sql_379C = '''
  select bbd_qyxx_id,count(distinct bbd_unique_id) as index_379C from dw.qyxx_jyyc
   where dt='{}' 
    and regexp_extract(busexcep_list,'(虚假|住所|经营场所)',1)!=''
    and
    rank_date>=to_date('{}')
    and 
    rank_date<to_date('{}')
    
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id  
'''.format(common_dt, before_1_year, current_date)
log("379C", sql_379C)
df_379C = spark.sql(sql_379C)

########################380C	qy_jyycYZCD_num_3year	企业经营异常数量严重程度近三年 #############################
sql_380C = '''
  select bbd_qyxx_id,count(distinct bbd_unique_id) as index_380C from dw.qyxx_jyyc
   where dt='{}' 
    and regexp_extract(busexcep_list,'(虚假|住所|经营场所)',1)!=''
    and
    rank_date>=to_date('{}')
    and 
    rank_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("380C", sql_380C)
df_380C = spark.sql(sql_380C)

########################381C	qy_jyycYZCD_num_5year	企业经营异常数量严重程度近五年 #############################
sql_381C = '''
  select bbd_qyxx_id,count(distinct bbd_unique_id) as index_381C from dw.qyxx_jyyc
   where dt='{}' 
    and regexp_extract(busexcep_list,'(虚假|住所|经营场所)',1)!=''
    and
    rank_date>=to_date('{}')
    and 
    rank_date<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("381C", sql_381C)
df_381C = spark.sql(sql_381C)

########################394C	qy_zl_num_3year	企业专利数量近三年#############################
sql_394C = '''
    select bbd_qyxx_id,count(distinct public_code) as index_394C from dw.qyxx_wanfang_zhuanli where dt='{}' 
    and publidate>=to_date('{}')
    and publidate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("394C", sql_394C)
df_394C = spark.sql(sql_394C)

########################395C	qy_zl_num_5year	企业专利数量近五年#############################
sql_395C = '''
    select bbd_qyxx_id,count(distinct public_code) as index_395C from dw.qyxx_wanfang_zhuanli where dt='{}' 
    and publidate>=to_date('{}')
    and publidate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("395C", sql_395C)
df_395C = spark.sql(sql_395C)

########################161C	qy_sb_num	企业商标数量#############################
sql_161C = '''
    select bbd_qyxx_id,count(distinct application_no) as index_161C from dw.xgxx_shangbiao 
    where dt='{}' 
    group by bbd_qyxx_id 
'''.format(common_dt)
log("161C", sql_161C)
df_161C = spark.sql(sql_161C)

########################396C	qy_zhaob_num_dim_1year	企业招标数量近一年#############################
sql_396C = '''
    select bbd_qyxx_id,count(distinct project_number) as index_396C from dw.shgy_zhaobjg where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("396C", sql_396C)
df_396C = spark.sql(sql_396C)

########################397C	qy_zhaob_num_dim_3year	企业招标数量近三年#############################
sql_397C = '''
    select bbd_qyxx_id,count(distinct project_number) as index_397C from dw.shgy_zhaobjg where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("397C", sql_397C)
df_397C = spark.sql(sql_397C)

########################398C	qy_zhaob_num_dim_3year	企业招标数量近三年#############################
sql_398C = '''
    select bbd_qyxx_id,count(distinct project_number) as index_398C from dw.shgy_zhaobjg where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("398C", sql_398C)
df_398C = spark.sql(sql_398C)

########################399C	qy_zhongb_num_dim_1year	企业中标数量近一年#############################
sql_399C = '''
    select bbd_qyxx_id,count(distinct project_number) as index_399C from dw.shgy_zhongbjg where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_1_year, current_date)
log("399C", sql_399C)
df_399C = spark.sql(sql_399C)

########################400C	qy_zhongb_num_dim_3year	企业中标数量近三年#############################
sql_400C = '''
    select bbd_qyxx_id,count(distinct project_number) as index_400C from dw.shgy_zhongbjg where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_3_year, current_date)
log("400C", sql_400C)
df_400C = spark.sql(sql_400C)

########################401C	qy_zhongb_num_dim_5year	企业中标数量近五年#############################
sql_401C = '''
    select bbd_qyxx_id,count(distinct project_number) as index_401C from dw.shgy_zhongbjg where dt='{}' 
    and 
    pubdate>=to_date('{}')
    and 
    pubdate<to_date('{}')
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt, before_5_year, current_date)
log("401C", sql_401C)
df_401C = spark.sql(sql_401C)

########################444C	qy_rz_num	企业软著数量#############################
sql_444C = '''
    select bbd_qyxx_id,count(distinct regnum) as index_444C from dw.rjzzq where dt='{}' 
    and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
    group by bbd_qyxx_id 
'''.format(common_dt)
log("444C", sql_444C)
df_444C = spark.sql(sql_444C)

########################402C	qy_deg1_jdktgg_num_1year	企业一度关联方借贷相关开庭公告数量近一年#############################
sql_402C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_402C from 
        (
        select bbd_qyxx_id,case_code from dw.ktgg where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        trial_date>=to_date('{}')
        and 
        trial_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
        
'''.format(common_dt, before_1_year, current_date)
log("402C", sql_402C)
df_402C = spark.sql(sql_402C)

########################403C	qy_deg1_jdktgg_num_3year	企业一度关联方借贷相关开庭公告数量近三年#############################
sql_403C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_403C from 
        (
        select bbd_qyxx_id,case_code from dw.ktgg where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        trial_date>=to_date('{}')
        and 
        trial_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("403C", sql_403C)
df_403C = spark.sql(sql_403C)

########################404C	qy_deg1_jdktgg_num_5year	企业一度关联方借贷相关开庭公告数量近五年#############################
sql_404C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_404C from 
        (
        select bbd_qyxx_id,case_code from dw.ktgg where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        trial_date>=to_date('{}')
        and 
        trial_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("404C", sql_404C)
df_404C = spark.sql(sql_404C)

########################426C	qy_deg2_jdktgg_num_1year	企业二度关联方借贷相关开庭公告数量近一年#############################
sql_426C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_426C from 
        (
        select bbd_qyxx_id,case_code from dw.ktgg where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        trial_date>=to_date('{}')
        and 
        trial_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_1_year, current_date)
log("426C", sql_426C)
df_426C = spark.sql(sql_426C)

########################427C	qy_deg2_jdktgg_num_3year	企业二度关联方借贷相关开庭公告数量近三年#############################
sql_427C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_427C from 
        (
        select bbd_qyxx_id,case_code from dw.ktgg where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        trial_date>=to_date('{}')
        and 
        trial_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("427C", sql_427C)
df_427C = spark.sql(sql_427C)

########################428C	qy_deg2_jdktgg_num_5year	企业二度关联方借贷相关开庭公告数量近五年#############################
sql_428C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_428C from 
        (
        select bbd_qyxx_id,case_code from dw.ktgg where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        trial_date>=to_date('{}')
        and 
        trial_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("428C", sql_428C)
df_428C = spark.sql(sql_428C)

########################408C	qy_deg1_jdcpws_num_1year	企业一度关联方借贷相关裁判文书数据近一年#############################
sql_408C = '''
        select R.bbd_qyxx_id,count(*) as index_408C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_adjudicative_documents where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )

        and
        sentence_date>=to_date('{}')
        and 
        sentence_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_1_year, current_date)
log("408C", sql_408C)
df_408C = spark.sql(sql_408C)

########################409C	qy_deg1_jdcpws_num_3year	企业一度关联方借贷相关裁判文书数据近三年#############################
sql_409C = '''
        select R.bbd_qyxx_id,count(*) as index_409C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_adjudicative_documents where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )

        and
        sentence_date>=to_date('{}')
        and 
        sentence_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("409C", sql_409C)
df_409C = spark.sql(sql_409C)

########################410C	qy_deg1_jdcpws_num_5year	企业一度关联方借贷相关裁判文书数据近五年#############################
sql_410C = '''
        select R.bbd_qyxx_id,count(*) as index_410C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_adjudicative_documents where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )
        and
        sentence_date>=to_date('{}')
        and 
        sentence_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("410C", sql_410C)
df_410C = spark.sql(sql_410C)

########################429C	qy_deg2_jdcpws_num_1year	企业二度关联方借贷相关裁判文书数据近一年#############################
sql_429C = '''
        select R.bbd_qyxx_id,count(*) as index_429C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_adjudicative_documents where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )

        and
        sentence_date>=to_date('{}')
        and 
        sentence_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_1_year, current_date)
log("429C", sql_429C)
df_429C = spark.sql(sql_429C)

########################430C	qy_deg2_jdcpws_num_3year	企业二度关联方借贷相关裁判文书数据近三年#############################
sql_430C = '''
        select R.bbd_qyxx_id,count(*) as index_430C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_adjudicative_documents where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )

        and
        sentence_date>=to_date('{}')
        and 
        sentence_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("430C", sql_430C)
df_430C = spark.sql(sql_430C)

########################431C	qy_deg2_jdcpws_num_5year	企业二度关联方借贷相关裁判文书数据近五年#############################
sql_431C = '''
        select R.bbd_qyxx_id,count(*) as index_431C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_adjudicative_documents where dt='{}' 
        and 
        (
        regexp_extract(action_cause,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or 
        regexp_extract(accuser,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        or
        regexp_extract(title,'(银行|分行|支行|小额贷款|信用卡|贷记卡|合同|买卖|担保|付款|借款|利息|结算|债权|借贷)',1)!=''
        )

        and
        sentence_date>=to_date('{}')
        and 
        sentence_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("431C", sql_431C)
df_431C = spark.sql(sql_431C)

########################308C	qy_deg1_bzxr_num	企业一度关联方被执行人数量#############################
sql_308C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_308C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_persons_subject_to_enforcement where dt='{}' 
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("308C", sql_308C)
df_308C = spark.sql(sql_308C)

########################414C	qy_deg1_bzxr_num_1year	企业一度关联方被执行人数量近一年#############################
sql_414C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_414C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_1_year, current_date)
log("414C", sql_414C)
df_414C = spark.sql(sql_414C)

########################415C	qy_deg1_bzxr_num_3year	企业一度关联方被执行人数量近三年#############################
sql_415C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_415C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("415C", sql_415C)
df_415C = spark.sql(sql_415C)

########################416C	qy_deg1_bzxr_num_5year	企业一度关联方被执行人数量近五年#############################
sql_416C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_416C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("416C", sql_416C)
df_416C = spark.sql(sql_416C)

########################446C	qy_deg2_frbzx_num_5year	二度关联方被执行人数量近五年#############################
sql_446C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_446C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("446C", sql_446C)
df_446C = spark.sql(sql_446C)

########################420C	qy_deg1_sxbzxr_num_1year	企业一度关联方失信被执行人数量近一年#############################
sql_420C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_420C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_dishonest_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_1_year, current_date)
log("420C", sql_420C)
df_420C = spark.sql(sql_420C)

########################421C	qy_deg1_sxbzxr_num_3year	企业一度关联方失信被执行人数量近三年#############################
sql_421C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_421C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_dishonest_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_3_year, current_date)
log("421C", sql_421C)
df_421C = spark.sql(sql_421C)

########################422C	qy_deg1_sxbzxr_num_5year	企业一度关联方失信被执行人数量近五年#############################
sql_422C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_422C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_dishonest_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("422C", sql_422C)
df_422C = spark.sql(sql_422C)

########################445C	qy_deg2_frsxbzx_num_5year	二度关联方失信被执行人数量近五年#############################
sql_445C = '''
        select R.bbd_qyxx_id,count(distinct case_code) as index_445C from 
        (
        select bbd_qyxx_id,case_code from dw.legal_dishonest_persons_subject_to_enforcement where dt='{}' 
        and
        register_date>=to_date('{}')
        and 
        register_date<to_date('{}')
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, before_5_year, current_date)
log("445C", sql_445C)
df_445C = spark.sql(sql_445C)

########################437C	qy_deg1_dxqy_num	企业一度关联方吊销企业数量#############################
sql_437C = '''
        select R.bbd_qyxx_id,count(*) as index_437C from 
        (
        select bbd_qyxx_id from dw.qyxx_basic where dt='{}' and company_enterprise_status='吊销'
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("437C", sql_437C)
df_437C = spark.sql(sql_437C)

########################438C	qy_deg2_dxqy_num	企业二度关联方吊销企业数量#############################
sql_438C = '''
        select R.bbd_qyxx_id,count(*) as index_438C from 
        (
        select bbd_qyxx_id from dw.qyxx_basic where dt='{}' and company_enterprise_status='吊销'
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("438C", sql_438C)
df_438C = spark.sql(sql_438C)

########################439C	qy_deg1_zx_num	企业一度关联方注销数量#############################
sql_439C = '''
        select R.bbd_qyxx_id,count(*) as index_439C from 
        (
        select bbd_qyxx_id from dw.qyxx_basic where dt='{}' and company_enterprise_status='注销'
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("439C", sql_439C)
df_439C = spark.sql(sql_439C)

########################356C	qy_deg2_zx_num	企业二度关联方注销数量#############################
sql_356C = '''
        select R.bbd_qyxx_id,count(*) as index_356C from 
        (
        select bbd_qyxx_id from dw.qyxx_basic where dt='{}' and company_enterprise_status='注销'
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("356C", sql_356C)
df_356C = spark.sql(sql_356C)

########################186C	qy_ssgd_num	企业上市股东数量#############################
sql_186C = '''
        select R.bbd_qyxx_id,count(*) as index_186C from 
        (
        select distinct bbd_qyxx_id from dw.qyxg_jqka_ipo_fxxg where dt='{}' 
        ) as L
        inner join 
        ( 
        select distinct bbd_qyxx_id,source_bbd_id as id from dw.off_line_relations where dt='{}' and  destination_degree=0 and relation_type='INVEST' and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
        ) as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, offline_relation_dt)
log("186C", sql_186C)
df_186C = spark.sql(sql_186C)

########################435C	qy_dxfzjg_num	企业吊销分支机构数量#############################
sql_435C = '''
        select R.bbd_qyxx_id,count(distinct R.id) as index_435C from 
        (
        select distinct bbd_qyxx_id from dw.qyxx_basic where dt='{}' and company_enterprise_status='吊销'
        ) as L
        inner join 
        ( 
        select distinct bbd_qyxx_id,bbd_branch_id as id from dw.qyxx_fzjg_merge where dt='{}'  and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
        ) as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, common_dt)
log("435C", sql_435C)
df_435C = spark.sql(sql_435C)

########################436C	qy_zxfzjg_num	企业注销分支机构数量#############################
sql_436C = '''
        select R.bbd_qyxx_id,count(distinct R.id) as index_436C from 
        (
        select distinct bbd_qyxx_id from dw.qyxx_basic where dt='{}' and company_enterprise_status='注销'
        ) as L
        inner join 
        ( 
        select distinct bbd_qyxx_id,bbd_branch_id as id from dw.qyxx_fzjg_merge where dt='{}'  and bbd_qyxx_id in (select bbd_qyxx_id from sample_id)
        ) as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt, common_dt)
log("436C", sql_436C)
df_436C = spark.sql(sql_436C)

########################320C	qy_deg1_xzcf_num	企业一度关联方行政处罚数量#############################
sql_320C = '''
        select R.bbd_qyxx_id,count(distinct punish_code) as index_320C from 
        (
        select bbd_qyxx_id,punish_code from dw.xzcf where dt='{}'
        ) as L
        inner join 
        degree1 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("320C", sql_320C)
df_320C = spark.sql(sql_320C)

########################353C	qy_deg2_xzcf_num	企业二度关联方行政处罚数量#############################
sql_353C = '''
        select R.bbd_qyxx_id,count(distinct punish_code) as index_353C from 
        (
        select bbd_qyxx_id,punish_code from dw.xzcf where dt='{}' 
        ) as L
        inner join 
        degree2 as R
        on L.bbd_qyxx_id=R.id
        group by R.bbd_qyxx_id
'''.format(common_dt)
log("353C", sql_353C)
df_353C = spark.sql(sql_353C)

########################进行结果汇总##############################

result = sample_id.join(df_10Y, 'bbd_qyxx_id', 'left') \
    .join(df_4B, 'bbd_qyxx_id', 'left') \
    .join(df_14Y, 'bbd_qyxx_id', 'left') \
    .join(df_11Y, 'bbd_qyxx_id', 'left') \
    .join(df_2Y, 'bbd_qyxx_id', 'left') \
    .join(df_368C, 'bbd_qyxx_id', 'left') \
    .join(df_369C, 'bbd_qyxx_id', 'left') \
    .join(df_370C, 'bbd_qyxx_id', 'left') \
    .join(df_371C, 'bbd_qyxx_id', 'left') \
    .join(df_372C, 'bbd_qyxx_id', 'left') \
    .join(df_373C, 'bbd_qyxx_id', 'left') \
    .join(df_441C, 'bbd_qyxx_id', 'left') \
    .join(df_22C, 'bbd_qyxx_id', 'left') \
    .join(df_374C, 'bbd_qyxx_id', 'left') \
    .join(df_375C, 'bbd_qyxx_id', 'left') \
    .join(df_376C, 'bbd_qyxx_id', 'left') \
    .join(df_377C, 'bbd_qyxx_id', 'left') \
    .join(df_378C, 'bbd_qyxx_id', 'left') \
    .join(df_379C, 'bbd_qyxx_id', 'left') \
    .join(df_380C, 'bbd_qyxx_id', 'left') \
    .join(df_381C, 'bbd_qyxx_id', 'left') \
    .join(df_382C, 'bbd_qyxx_id', 'left') \
    .join(df_383C, 'bbd_qyxx_id', 'left') \
    .join(df_123C, 'bbd_qyxx_id', 'left') \
    .join(df_384C, 'bbd_qyxx_id', 'left') \
    .join(df_385C, 'bbd_qyxx_id', 'left') \
    .join(df_113C, 'bbd_qyxx_id', 'left') \
    .join(df_386C, 'bbd_qyxx_id', 'left') \
    .join(df_387C, 'bbd_qyxx_id', 'left') \
    .join(df_110C, 'bbd_qyxx_id', 'left') \
    .join(df_440C, 'bbd_qyxx_id', 'left') \
    .join(df_104C, 'bbd_qyxx_id', 'left') \
    .join(df_388C, 'bbd_qyxx_id', 'left') \
    .join(df_389C, 'bbd_qyxx_id', 'left') \
    .join(df_282C, 'bbd_qyxx_id', 'left') \
    .join(df_390C, 'bbd_qyxx_id', 'left') \
    .join(df_391C, 'bbd_qyxx_id', 'left') \
    .join(df_270C, 'bbd_qyxx_id', 'left') \
    .join(df_392C, 'bbd_qyxx_id', 'left') \
    .join(df_393C, 'bbd_qyxx_id', 'left') \
    .join(df_432C, 'bbd_qyxx_id', 'left') \
    .join(df_433C, 'bbd_qyxx_id', 'left') \
    .join(df_434C, 'bbd_qyxx_id', 'left') \
    .join(df_296C, 'bbd_qyxx_id', 'left') \
    .join(df_394C, 'bbd_qyxx_id', 'left') \
    .join(df_395C, 'bbd_qyxx_id', 'left') \
    .join(df_161C, 'bbd_qyxx_id', 'left') \
    .join(df_396C, 'bbd_qyxx_id', 'left') \
    .join(df_397C, 'bbd_qyxx_id', 'left') \
    .join(df_398C, 'bbd_qyxx_id', 'left') \
    .join(df_399C, 'bbd_qyxx_id', 'left') \
    .join(df_400C, 'bbd_qyxx_id', 'left') \
    .join(df_401C, 'bbd_qyxx_id', 'left') \
    .join(df_444C, 'bbd_qyxx_id', 'left') \
    .join(df_402C, 'bbd_qyxx_id', 'left') \
    .join(df_403C, 'bbd_qyxx_id', 'left') \
    .join(df_404C, 'bbd_qyxx_id', 'left') \
    .join(df_408C, 'bbd_qyxx_id', 'left') \
    .join(df_409C, 'bbd_qyxx_id', 'left') \
    .join(df_410C, 'bbd_qyxx_id', 'left') \
    .join(df_308C, 'bbd_qyxx_id', 'left') \
    .join(df_414C, 'bbd_qyxx_id', 'left') \
    .join(df_415C, 'bbd_qyxx_id', 'left') \
    .join(df_416C, 'bbd_qyxx_id', 'left') \
    .join(df_420C, 'bbd_qyxx_id', 'left') \
    .join(df_421C, 'bbd_qyxx_id', 'left') \
    .join(df_422C, 'bbd_qyxx_id', 'left') \
    .join(df_437C, 'bbd_qyxx_id', 'left') \
    .join(df_438C, 'bbd_qyxx_id', 'left') \
    .join(df_439C, 'bbd_qyxx_id', 'left') \
    .join(df_356C, 'bbd_qyxx_id', 'left') \
    .join(df_186C, 'bbd_qyxx_id', 'left') \
    .join(df_435C, 'bbd_qyxx_id', 'left') \
    .join(df_436C, 'bbd_qyxx_id', 'left') \
    .join(df_426C, 'bbd_qyxx_id', 'left') \
    .join(df_427C, 'bbd_qyxx_id', 'left') \
    .join(df_428C, 'bbd_qyxx_id', 'left') \
    .join(df_429C, 'bbd_qyxx_id', 'left') \
    .join(df_430C, 'bbd_qyxx_id', 'left') \
    .join(df_431C, 'bbd_qyxx_id', 'left') \
    .join(df_320C, 'bbd_qyxx_id', 'left') \
    .join(df_353C, 'bbd_qyxx_id', 'left') \
    .join(df_445C, 'bbd_qyxx_id', 'left') \
    .join(df_446C, 'bbd_qyxx_id', 'left')

###################结果处理，将数值型的列中的null(未join上导致的)填充为0#################################
rs = result.fillna(
    {
        'index_368C': 0,
        'index_369C': 0,
        'index_370C': 0,
        'index_371C': 0,
        'index_372C': 0,
        'index_373C': 0,
        'index_441C': 0,
        'index_22C': 0,
        'index_374C': 0,
        'index_375C': 0,
        'index_376C': 0,
        'index_377C': 0,
        'index_378C': 0,
        'index_379C': 0,
        'index_380C': 0,
        'index_381C': 0,
        'index_382C': 0,
        'index_383C': 0,
        'index_123C': 0,
        'index_384C': 0,
        'index_385C': 0,
        'index_113C': 0,
        'index_386C': 0,
        'index_387C': 0,
        'index_110C': 0,
        'index_440C': 0,
        'index_104C': 0,
        'index_388C': 0,
        'index_389C': 0,
        'index_282C': 0,
        'index_390C': 0,
        'index_391C': 0,
        'index_270C': 0,
        'index_392C': 0,
        'index_393C': 0,
        'index_432C': 0,
        'index_433C': 0,
        'index_434C': 0,
        'index_296C': 0,
        'index_394C': 0,
        'index_395C': 0,
        'index_161C': 0,
        'index_396C': 0,
        'index_397C': 0,
        'index_398C': 0,
        'index_399C': 0,
        'index_400C': 0,
        'index_401C': 0,
        'index_444C': 0,
        'index_402C': 0,
        'index_403C': 0,
        'index_404C': 0,
        'index_408C': 0,
        'index_409C': 0,
        'index_410C': 0,
        'index_308C': 0,
        'index_414C': 0,
        'index_415C': 0,
        'index_416C': 0,
        'index_420C': 0,
        'index_421C': 0,
        'index_422C': 0,
        'index_437C': 0,
        'index_438C': 0,
        'index_439C': 0,
        'index_356C': 0,
        'index_186C': 0,
        'index_435C': 0,
        'index_436C': 0,
        'index_426C': 0,
        'index_427C': 0,
        'index_428C': 0,
        'index_429C': 0,
        'index_430C': 0,
        'index_431C': 0,
        'index_320C': 0,
        'index_353C': 0,
        'index_445C': 0,
        'index_446C': 0
    }
)
##############################输出结果#############################
rs.show()
rs.write.csv('/user/dptest/{}/indexs/derive'.format(time.strftime("%Y-%m-%d")), mode='overwrite', header=True)

spark.stop()
