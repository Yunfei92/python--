import requests
import xlwt
from bs4 import BeautifulSoup
a=[]
global count2
url = 'http://news.163.com/rank/'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'gb2312'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')
# kinds=soup.select('div.titleBar')
titles = soup.select('.area.areabg1 tr td a')
counts=soup.select('.tabContents .cBlue')
for i in range(len(titles)):
    title=(titles[i])
    count3=(counts[i])
    datas=[ title.get_text(),count3.get_text(),title['href']]
    a.append(datas)
file_path = 'D:\\网易新闻排行榜.xlsx'
#新建一个excell文件
wb = xlwt.Workbook()
#创建一个工作薄
sheet = wb.add_sheet('网易新闻排行榜')  # sheet的名称为test
row_count = len(a)
col_count = len(a[0])
for row in range(0, row_count):
    col_count = len(a[row])
    for col in range(0, col_count):
        sheet.write(row, col, a[row][col])
wb.save(file_path)
