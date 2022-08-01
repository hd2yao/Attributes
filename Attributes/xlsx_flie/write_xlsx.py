import pandas as pd
from Attributes.attributes_Generator.n_norm import attributesGenerator


def xlsx_file(axis, filename, sheet):
    data = pd.DataFrame(axis)
    writer = pd.ExcelWriter(filename)
    data.to_excel(writer, sheet)

    writer.save()
    writer.close()


if __name__ == '__main__':
    axis = attributesGenerator(127.5, 1806.25, 32, 100)
    xlsx_file(axis, "axis_pycharm_test.xlsx", "sheet1")
    # 可能会有以下提示（warn 不用管）
    # D:\Anaconda\lib\site - packages\xlsxwriter\workbook.py: 329: UserWarning: Calling close() on already closed file.
    # warn("Calling close() on already closed file.")
