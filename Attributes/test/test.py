import time

import scipy.stats
import numpy as np
import array

from Attributes.rarity.rarity import rarity
from Attributes.xlsx_flie.write_xlsx import xlsx_file


def n_norm(mean, variance, dimension):
    # 均值
    meanMatrix = np.full((1, dimension), mean)
    meanMatrix = meanMatrix[0]
    # 协方差矩阵
    convMatrix = np.diag([variance] * dimension)
    return meanMatrix, convMatrix


def n_normGenerator(meanMatrix, convMatrix, size):
    axis = np.random.multivariate_normal(
        mean=meanMatrix, cov=convMatrix, size=size)
    # pandas取整数
    # pandas转成uint8
    axis = axis.astype("uint8")
    return axis


def attributesGenerator(mean, variance, dimension, size):
    meanMatrix, convMatrix = n_norm(mean, variance, dimension)
    axis = n_normGenerator(meanMatrix, convMatrix, size)
    return axis


def calculateFx(dataMatrix, meanMatrix, convMatrix):
    cdfMatrix = scipy.stats.multivariate_normal.cdf(dataMatrix, meanMatrix, convMatrix)
    # pdfMatrix = scipy.stats.multivariate_normal.pdf(0.2, meanMatrix, meanMatrix)
    result = 1 - cdfMatrix
    # print(result)
    return result


def arrayF(axis, meanMatrix, convMatrix):
    resultList = []
    for i in range(len(axis)):
        valueF = calculateFx(axis[i], meanMatrix, convMatrix)
        resultList.append(valueF)
    return resultList


def listSort(flist):
    ordered_list = sorted(flist)
    print(ordered_list)
    return ordered_list


def rarity(value):
    countSSR = 0
    countSR = 0
    countR = 0
    countN = 0
    if value <= 0.35:
        if value <= 0.05:
            # print("SSR")
            countSSR += 1
        elif 0.15 >= value > 0.05:
            countSR += 1
        elif 0.35 >= value > 0.15:
            countR += 1
    else:
        countN += 1


if __name__ == '__main__':
    start_time = time.time()
    meanMatrix = np.full((1, 32), 127.5)
    meanMatrix = meanMatrix[0]
    convMatrix = np.diag([10000000] * 32)

    axis = attributesGenerator(127.5, 42.5, 32, 3000)
    axis = np.array(axis)

    resultFList = arrayF(axis, meanMatrix, convMatrix)
    print(resultFList)
    resultFList = listSort(resultFList)
    xlsx_file(resultFList, "axis_sortResult_3k.xlsx", "sheet1")
    end_time = time.time()
    print("总用时", end_time-start_time)

    # countSSR = 0
    # countSR = 0
    # countR = 0
    # countN = 0
    # for i in range(len(axis)):
    #     valueF = calculateFx(axis[i], meanMatrix, convMatrix)
    #     if valueF <= 0.35:
    #         if valueF <= 0.05:
    #             # print("SSR")
    #             countSSR += 1
    #         elif 0.15 >= valueF > 0.05:
    #             countSR += 1
    #         elif 0.35 >= valueF > 0.15:
    #             countR += 1
    #     else:
    #         countN += 1
    #     # rarity(valueF)
    #
    # print("SSR =", countSSR)
    # print("SR =", countSR)
    # print("R =", countR)
    # print("N =", countN)
