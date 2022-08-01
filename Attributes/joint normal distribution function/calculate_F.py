import scipy.stats
import numpy as np

from Attributes.rarity.rarity import rarity


def calculateFx(dataMatrix, meanMatrix, convMatrix):
    cdfMatrix = scipy.stats.multivariate_normal.cdf(dataMatrix, meanMatrix, convMatrix)
    # pdfMatrix = scipy.stats.multivariate_normal.pdf(0.2, meanMatrix, meanMatrix)
    print(cdfMatrix)
    # print(pdfMatrix)
    print(1 - cdfMatrix)
    return 1 - cdfMatrix


if __name__ == '__main__':
    meanMatrix = np.full((1, 32), 127.5)
    meanMatrix = meanMatrix[0]
    # 协方差矩阵
    convMatrix = np.diag([1806.25] * 32)

    dataMatrix = [140, 118, 95, 132, 125, 120, 172, 176, 185, 109, 200, 84, 55, 228, 114, 152, 145, 96, 69, 149, 145,
                  140, 108, 68, 52, 98, 154, 128, 104, 122, 118, 209]
    dataMatrix1 = [187, 145, 199, 126, 161, 127, 94, 107, 89, 139, 134, 113, 159, 171, 153, 126, 188, 59, 107, 209, 142,
                   146, 138, 37, 156, 170, 64, 159, 79, 111, 0, 111]
    dataMatrix2 = [173, 100, 89, 189, 88, 177, 100, 116, 131, 141, 99, 82, 152, 117, 176, 51, 105, 162, 127, 77, 105,
                   229, 157, 150, 41, 195, 80, 163, 89, 55, 130, 136]
    dataMatrix_test = [127.5, 127.5, 127.5, 127.5, 127.5, 127.5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                       255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]

    valueF = calculateFx(dataMatrix, meanMatrix, convMatrix)
    rarity(valueF)
    # print(1/valueF)
