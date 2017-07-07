import xlsxwriter

workbook = xlsxwriter.Workbook("xlsx_test.xlsx") # 创建一个名为 xlsx_test.xlsx 的工作薄
worksheet1 = workbook.add_worksheet("ID") # 新增一个工作表,可传入表名，不传默认为sheet1
worksheet2 = workbook.add_worksheet("姓名") # 重复命令可新增多张数据表

# 设置列的参数，20，10代表字符数
worksheet1.set_column("A:A", 20)
worksheet1.set_column('B:B', 10)

# 插入数据，传入三个参数
worksheet1.write(0, 0, "hello world!") # 三个参数分别为：行，列，数据。注意行列索引值从零开始。

# 最后要关闭工作薄，完成数据的保存
workbook.close()