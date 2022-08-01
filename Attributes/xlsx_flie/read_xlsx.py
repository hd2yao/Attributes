import numpy as np
import xlrd


def readExcel(filename):
    # 先声明一个空list
    resArray = []
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    for i in range(table.nrows):  # table.nrows表示总行数
        line = table.row_values(i)  # 读取每行数据，保存在line里面，line是list
        resArray.append(line)  # 将line加入到resArray中，resArray是二维list
    resArray = np.array(resArray)  # 将resArray从二维list变成数组
    # print(resArray)
    return resArray


if __name__ == '__main__':
    rowsArray = readExcel("axis_pycharm_test.xlsx")







