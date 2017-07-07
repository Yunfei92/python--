import requests
import xlwt
from bs4 import BeautifulSoup
data=[]
link=[]
def get_Title(url):
    #获取数据集
    res=requests.get(url)
    #编码格式为utf-8
    res.encoding='utf-8'
    #使用剖析器为html.parser
    soup=BeautifulSoup(res.text,'html.parser')
    #获取新闻标题
    titles=soup.select('.c-title')
    #print(titles)
    for i in range(len(titles)):
        title=titles[i]
        datas = [title.get_text()]
        data.append(datas)
        #print(title.get_text())
    file_path = 'D:\\搜索数据集.xlsx'
    # 新建一个excell文件
    wb = xlwt.Workbook()
    # 创建一个工作薄
    sheet = wb.add_sheet('数据集')  # sheet的名称为test
    row_count = len(data)
    col_count = len(data[0])
    for row in range(0, row_count):
        col_count = len(data[row])
        for col in range(0, col_count):
            sheet.write(row, col, data[row][col])
    wb.save(file_path)
'''
#获取底部分页链接
def get_Links(startUrl):
    # 获取链接集合
    res = requests.get(startUrl)
    # 编码格式为utf-8
    res.encoding = 'utf-8'
    # 使用剖析器为html.parser
    soup = BeautifulSoup(res.text, 'html.parser')
    hrefs=soup.select('#page a')
    for i in range(len(hrefs)):
        href=hrefs[i]
        link.append('http://news.baidu.com'+href['href'])
    print(link)
    return link
        #get_Title('http://news.baidu.com'+href['href'])
        #print('news.baidu.com'+href['href'])
'''
#调用函数
for i in range(0,10000,20):
    #打印链接集合
    print('http://news.baidu.com/ns?word=python&pn={0}&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page=1'.format(i))
    get_Title('http://news.baidu.com/ns?word=python&pn={0}&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page=1'.format(i))
'''
link=get_Links('http://news.baidu.com/ns?word=python&tn=news&from=news&cl=2&rn=20&ct=1')
for i in link:
    get_Title(i)
'''