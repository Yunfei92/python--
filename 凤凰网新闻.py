import requests
import xlwt
from bs4 import BeautifulSoup
a={}
b=[]
c=[]
url = 'http://news.ifeng.com/hotnews/'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'UTF-8'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')
news=soup.select('.tab_01 tr td ')
# titles=soup.select('.tab_01 h3 a')
#遍历每一个class=tab_01的节点
for title in news:
    datas=[title.get_text()]
    print(datas)
# for i in (range(0,len(a),5)):
#     b=[a[i]]
# c.append(b)
print(a)
# file_path = 'D:\\text.xlsx'
# #新建一个excell文件
# wb = xlwt.Workbook()
# #创建一个工作薄
# sheet = wb.add_sheet('凤凰网排行榜')  # sheet的名称为test
# row_count = len(a)
# col_count = len(a[0])
# for row in range(0, row_count):
#     col_count = len(a[row])
#     for col in range(0, col_count):
#         sheet.write(row, col, a[row][col])
# wb.save(file_path)

##c01 > table > tbody > tr:nth-child(2) > td:nth-child(3)
##c01 > table > tbody > tr:nth-child(2) > td:nth-child(4)