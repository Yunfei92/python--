
import time
from selenium import webdriver
import requests
import xlwt
from bs4 import BeautifulSoup
data=[]
driver = webdriver.Chrome()  # 打开chrome
driver.maximize_window()  # 最大化浏览器窗口
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://news.baidu.com/")  # 地址栏输入百度新闻地址
driver.find_element_by_id("ww").send_keys("python")  # 搜索输入框输入python
driver.find_element_by_class_name("btn").click()  # 点击百度一下按钮

# 导入time模块，等待2秒

time.sleep(2)
for i in range(30):
    driver.find_element_by_link_text("下一页>").click()
    time.sleep(2)

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


#调用函数
for i in range(0,500,20):
    get_Title('http://news.baidu.com/ns?word=python&pn={0}&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page=1'.format(i))



#关闭浏览器
driver.close()