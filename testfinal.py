import xlwt
import xlrd
import time
import re
from selenium import webdriver

data=[]
i=0
def get_Search(keyword):
    driver = webdriver.Chrome()  # 打开chrome
    driver.maximize_window()  # 最大化浏览器窗口
    driver.implicitly_wait(3)  # 设置隐式时间等待
    driver.get("http://www.baidu.com/")  # 地址栏输入百度新闻地址
    search_form = driver.find_element_by_id("kw")
    search_form.send_keys(keyword)  # 搜索输入框输入keyword
    driver.find_element_by_id("su").click()  # 点击百度一下按钮
    text=driver.find_elements_by_css_selector("#s_tab a")
    text[0].click()
    driver.find_element_by_id("search_type_radio_title").click()  # 点击百度一下标题按钮
    # 导入time模块，等待2秒
    time.sleep(2)
    #获取搜索数据的总量
    text=driver.find_element_by_class_name("nums").text
    print(text)
    #定义正则匹配数字
    pattern=re.findall(r'[0-9]',text)
    #将数据列表转换为字符串
    str = ('').join(pattern)
    result=int(str)/100+1
    count=int(result)
    #for循环控制点击下一页的次数
    for k in range(count):
        # for循环获取每一页的文本数据
        for j in range(0, 19):
            text1 =[driver.find_elements_by_class_name("c-title")[j].text]
            print(text1)
            text2=[driver.find_elements_by_class_name("c-title-author")[j].text]
            print(text2)
            data.append([text1,text2])

        file_path = 'G:\文献与研究\20161202资本结构动态调整\002_媒体关注度\03数据\爬虫\result.xls'
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
        driver.find_element_by_link_text("下一页>").click()
        time.sleep(2)
    # 关闭浏览器
    driver.close()
#调用函数

keywords=[]
data = xlrd.open_workbook("test.xls") #打开excel
table = data.sheets()[0]   #选择工作表
nrows = table.nrows    #行数
for i in range(0,nrows):
    rValues= table.cell(i, 0).value  #对单元格取值
    keywords.append(rValues)
for keyword in keywords:
    get_Search(keyword)

