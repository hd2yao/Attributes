import numpy as np


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


if __name__ == '__main__':
    attributesGenerator(127.5, 180.25, 32, 10000)
