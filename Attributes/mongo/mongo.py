import xlrd
import json
import pymongo


# 连接数据库
def mongo_connect(database, collection, filename):
    client = pymongo.MongoClient('localhost', 27017)
    mydb = client[database]
    info = mydb[collection]
    # 读取Excel文件
    data3 = xlrd.open_workbook(filename)
    table = data3.sheets()[0]
    # 读取excel第一行数据作为存入mongodb的字段名
    rowsTag = table.row_values(0)
    nRows = table.nrows
    returnData = {}

    for i in range(1, nRows):
        # 将字段名和excel数据存储为字典形式，并转换为json格式
        returnData[i] = json.dumps(dict(zip(rowsTag, table.row_values(i))))
        # 通过编解码还原数据
        returnData[i] = json.loads(returnData[i])
        info.insert_one(returnData[i])
