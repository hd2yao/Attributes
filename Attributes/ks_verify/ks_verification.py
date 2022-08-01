from scipy import stats
import pandas as pd
import numpy as np
from Attributes.attributes_Generator.n_norm import attributesGenerator

# .kstest方法：KS检验，参数分别是：待检验的数据，检验方法（这里设置成norm正态分布），均值与标准差
# 结果返回两个值：statistic → D值，pvalue → P值
# p值大于0.05，为正态分布


def ks(array):
    df = pd.DataFrame(array, columns=['value'])
    u = df['value'].mean()  # 计算均值
    std = df['value'].std()  # 计算标准差
    statistic, pvalue = stats.kstest(df['value'], 'norm', (u, std))
    # print("statistic = ", statistic)
    print("pvalue = ", pvalue)
    if pvalue > 0.05:
        print("输入的数据服从正态分布")
    # KstestResult(statistic=0.08765610379602129, pvalue=0.9484434034097077)


if __name__ == '__main__':
    data = [140, 118, 95, 132, 125, 120, 172, 176, 185, 109, 200, 84, 55, 228, 114, 152, 145, 96, 69, 149, 145, 140,
            108, 68, 52, 98, 154, 128, 104, 122, 118, 209]

    meanMatrix = np.full((1, 32), 127.5)
    meanMatrix = meanMatrix[0]
    # 协方差矩阵
    convMatrix = np.diag([1806.25] * 32)
    axis = attributesGenerator(127.5, 42.5, 32, 30)
    axis = np.array(axis)
    for i in range(len(axis)):
        ks(axis[i])

    # ks(data)
