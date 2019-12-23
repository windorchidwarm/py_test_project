import requests
import time
from pyspark.sql import SparkSession

warehouseLocation = "hdfs:///user/hive/warehouse"
spark = SparkSession \
    .builder \
    .appName("index_fetch1") \
    .config("spark.sql.warehouse.dir", warehouseLocation) \
    .enableHiveSupport() \
    .getOrCreate()


def getdata(lines):
    index = ["368C", "369C", "370C", "371C", "372C", "373C", "441C", "22C", "374C", "375C", "376C", "377C", "378C", "379C", "380C", "381C", "382C", "383C", "123C", "384C", "385C", "113C", "386C", "387C", "110C", "440C", "104C", "388C",
             "389C", "282C", "390C", "391C", "270C", "392C", "393C", "432C", "433C", "434C", "296C", "394C", "395C", "161C", "396C", "397C", "399C", "400C", "401C", "444C", "402C", "403C", "404C", "408C", "409C", "410C", "308C", "414C",
             "415C", "416C", "420C", "421C", "422C", "437C", "438C", "439C", "356C", "186C", "435C", "436C", "426C", "427C", "428C", "429C", "430C", "431C", "320C", "353C", "445C", "446C"]
    body = {
        "indexCodes": index,
        "qyIds": [line["bbd_qyxx_id"] for line in lines]
    }

    url = "http://bbddw.api.bbdops.com/api/bob/1/indexResult/specific"

    rs = requests.post(url=url, json=body)
    if rs and rs.status_code == 200:
        datas = rs.json()["data"]
        result = []
        for x in datas:
            one = {}
            one["bbd_qyxx_id"] = x["qyId"]
            for k in index:
                one["index_" + k] = x["indexCodes"][k]
            result.append(one)
        return result
    else:
        return []


######################目标企业##########################

sample_id = spark.read.csv('/user/dptest/ids', header=True, sep=',')
sample_id.createOrReplaceTempView('sample_id')

df = sample_id.select("bbd_qyxx_id").rdd.mapPartitions(getdata)
index_api_data = spark.createDataFrame(df, samplingRatio=1)
index_api_data.createOrReplaceTempView("index_api_data")
index_api_data.show()

dt = '2019-09-10'
index_test_data = spark.read.csv('/user/dptest/{}/indexs'.format(dt), header=True, sep=',')
index_test_data.createOrReplaceTempView("index_test_data")

keys = index_api_data.columns
keys.remove("bbd_qyxx_id")
print("==========================================对比的keys====================")
print(keys)

sql = '''
        select L.bbd_qyxx_id,{} from index_api_data as L inner join indexhadoo_test_data as R on L.bbd_qyxx_id=R.bbd_qyxx_id
    '''.format(",".join(["concat(L.{},R.{},L.{}=R.{}) as {}_result".format(k, k, k, k, k) for k in keys]))

print(sql)
compare_result = spark.sql(sql)
compare_result.show()
compare_result.write.csv('/user/dptest/{}/compare'.format(time.strftime("%Y-%m-%d")), mode='overwrite', header=True)

spark.stop()
