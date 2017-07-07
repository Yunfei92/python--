import requests
import xlwt
from xlutils.copy import copy
import xlrd as ExcelRead
from bs4 import BeautifulSoup
a=[]
def get_data(url):
# url = 'http://news.people.com.cn/GB/124658/index.html'
    res = requests.get(url)
    # 使用UTF-8编码
    res.encoding = 'GB2312'
    # 使用剖析器为html.parser
    soup = BeautifulSoup(res.text, 'html.parser')
    #获取新闻标题列表
    titles = soup.select('a.anavy')
    for i in range(len(titles)):
        title=(titles[i])
        datas=[title.get_text(),title['href']]
        a.append(datas)
    # print(a)
    file_path = 'D:\\人民网排行榜.xls'
    #新建一个excell文件
    wb = xlwt.Workbook()
    #创建一个工作薄
    sheet = wb.add_sheet('人民网排行榜')  # sheet的名称为test
    row_count = len(a)
    col_count = len(a[0])
    for row in range(0, row_count):
        for col in range(0, col_count):
            sheet.write(row, col, a[row][col])
            # print(sheet)
    wb.save(file_path)
def write_append():
    filename = "D:\\人民网排行榜.xls"
    r_xls = ExcelRead.open_workbook(filename)
    r_sheet = r_xls.sheet_by_index(0)
    rows = r_sheet.nrows
    w_xls = copy(r_xls)
    sheet = w_xls.get_sheet(0)
    url = 'http://news.people.com.cn/GB/124658/index.html'
    res = requests.get(url)
    # 使用UTF-8编码
    res.encoding = 'GB2312'

    # 使用剖析器为html.parser
    soup = BeautifulSoup(res.text, 'html.parser')

    # 获取新闻标题列表
    titles = soup.select('a.anavy')
    for i in range(len(titles)):
        title = (titles[i])
        datas = [title.get_text(), title['href']]
        a.append(datas)
    row_count = len(a)
    col_count = len(a[0])
    for row in range(0, row_count):
        for col in range(0, col_count):
            sheet.write(row + rows, col, a[row][col])

    w_xls.save(filename)
    # values = ["Ann", "woman", 22, "UK"]
    #
    # r_xls = ExcelRead.open_workbook(filename)
    # r_sheet = r_xls.sheet_by_index(0)
    # rows = r_sheet.nrows
    # w_xls = copy(r_xls)
    # sheet_write = w_xls.get_sheet(0)
    #
    # for i in range(0, len(values)):
    #     sheet_write.write(rows, i, values[i])
    #     rows += 1
    #
    # w_xls.save(filename )
#回调函数
if __name__ == "__main__":
   # get_data('http://news.people.com.cn/GB/124658/index.html')
   write_append()


