import time

import numpy as np
from Attributes.xlsx_flie.read_xlsx import readExcel
from Attributes.attributes_Generator.n_norm import attributesGenerator

# 传入的两个维数要相同，并且 x,y 的交集是维数，而不是真正的交集
from Attributes.xlsx_flie.write_xlsx import xlsx_file


def JaccardDistance(x, y):
    x = np.asarray(x, np.int32)
    y = np.asarray(y, np.int32)
    ab = np.double(np.bitwise_and((x != y), np.bitwise_or(x != 0, y != 0)).sum())
    a_b = np.double(np.bitwise_or(x != 0, y != 0).sum())
    # return np.double(np.bitwise_and((x != y), np.bitwise_or(x != 0, y != 0)).sum()) / np.double(
    #     np.bitwise_or(x != 0, y != 0).sum())
    # print(ab, a_b)
    return ab / a_b


def Jaccard(a, b):
    ab = len(set(a).intersection(set(b)))
    a_b = len(set(a).union(set(b)))
    if a_b == 0:
        return 0
    # print(ab, a_b)
    else:
        return len(set(a).intersection(set(b))) / len(set(a).union(set(b)))


def JaccardModel(rowsArray):
    # 获取 SR 特征
    rowsSet = []
    for i in range(len(rowsArray)):
        rowSet = []
        for j in range(len(rowsArray[i])):

            if rowsArray[i][j] > 170:
                rowSet.append(j + 1)
        rowsSet.append(rowSet)
    # print(rowsSet)
    # print(len(rowsSet))
    # print(rowsSet[3])

    # 计算 1-jd （Jaccard Distance）
    jdRowsSet = []
    for i in range(len(rowsSet)):
        jdRowSet = []
        for j in range(len(rowsSet)):
            if i != j:
                jd = Jaccard(rowsSet[i], rowsSet[j])
                jdRowSet.append(1 - jd)
        jdRowsSet.append(jdRowSet)
    # print(jdRowsSet)
    # print(len(jdRowsSet[45]))
    # print(jdRowsSet[45])

    # 获取 1-jd 的范围
    # print(max(map(max, jdRowsSet)))
    # print(min(map(min, jdRowsSet)))
    jdMax = np.max(jdRowsSet)
    jdMin = np.min(jdRowsSet)

    #  求平均值
    jdRowsAverage = []
    for i in range(len(jdRowsSet)):
        average = sum(jdRowsSet[i]) / len(jdRowsSet)
        jdRowsAverage.append(average)
    # print(jdRowsAverage)
    # print(len(jdRowsAverage))

    # 归一化
    zScoreSet = []
    for i in range(len(jdRowsAverage)):
        zScore = (jdRowsAverage[i] - jdMin) / (jdMax - jdMin)
        zScoreSet.append(zScore)
    # print(zScoreSet)
    # print(len(zScoreSet))

    # 稀有度分数
    scoreSet = []
    for i in range(len(zScoreSet)):
        score = zScoreSet[i] * 100
        scoreSet.append(score)
    # print(scoreSet)
    # print(len(scoreSet))

    # 排序
    scoreSortSet = sorted(scoreSet, reverse=True)
    # print(scoreSortSet)
    # print(len(scoreSortSet))
    return scoreSortSet


if __name__ == '__main__':
    # x = ["trait_2", "trait_4", "trait_6", "trait_21"]
    # y = ["trait_2", "trait_4", "trait_16", "trait_22", "trait_28"]
    #
    # x1 = [2, 4, 6, 21, 22]
    # y1 = [2, 4, 16, 22, 28]
    #
    # jd1 = Jaccard(x1, y1)
    # print(jd1)

    start_time = time.time()
    # 随机生成数据(也可以不用写入excel）
    axis = attributesGenerator(127.5, 1806.25, 32, 10000)
    # xlsx_file(axis, "axis_pycharm_test.xlsx", "sheet1")

    # 文件不在当前目录下，要用绝对路径
    # 'D:\\PyCharm\\PycharmProjects\\pythonProject\\Attributes\\xlsx_flie\\axis_pycharm_test.xlsx'
    # rows = readExcel('axis_pycharm_test.xlsx')
    # JaccardModel(rows)

    jdModelSet = JaccardModel(axis)
    xlsx_file(jdModelSet, "axis_jdModel_sorted.xlsx", "sheet1")

    end_time = time.time()
    print("总耗时", end_time - start_time)
