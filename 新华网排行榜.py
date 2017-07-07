import requests
import xlwt
from bs4 import BeautifulSoup
a=[]
url = 'http://www.xinhuanet.com/newscenter/xwph.htm'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'gb2312'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')

titles=soup.select('a.black12')
#遍历
for title in titles:
    datas=[title.get_text(),title['href']]
    a.append(datas)
#     f = open(r'D:\新华网0324.txt','a',encoding='utf-8')
#     f.write(title.get_text()+'\n')
#     f.close()
file_path = 'D:\\新华网排行榜.xlsx'
#新建一个excell文件
wb = xlwt.Workbook()
#创建一个工作薄
sheet = wb.add_sheet('新华网排行榜')  # sheet的名称为test
row_count = len(a)
col_count = len(a[0])
for row in range(0, row_count):
    col_count = len(a[row])
    for col in range(0, col_count):
        sheet.write(row, col, a[row][col])
wb.save(file_path)