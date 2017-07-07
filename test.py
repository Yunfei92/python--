import xlwt
import time
from selenium import webdriver

def get_Search(keyword):
    data = []

    driver = webdriver.Chrome()  # 打开chrome
    driver.maximize_window()  # 最大化浏览器窗口
    driver.implicitly_wait(3)  # 设置隐式时间等待
    driver.get("http://www.baidu.com/")  # 地址栏输入百度新闻地址
    search_form = driver.find_element_by_id("kw")
    search_form.send_keys(keyword)  # 搜索输入框输入keyword
    driver.find_element_by_id("su").click()  # 点击百度一下按钮
    text=driver.find_elements_by_css_selector("#s_tab a")
    text[0].click()
    text1=driver.find_element_by_id("search_type_radio_title")
    text1.click()
    # 导入time模块，等待2秒
    time.sleep(2)

    #获取搜索数据的总量
    #text=driver.find_element_by_class_name("nums").text
    #print(text)
    #定义正则匹配数字
    #pattern=re.findall(r'[0-9]',text)
    #将数据列表转换为字符串
   # str = ('').join(pattern)
    #result=int(str)/100+1
    #count=int(result)

    #for循环控制点击下一页的次数
    for k in range(38):
        count1 = driver.find_elements_by_class_name("c-title-author")
        print(len(count1))

        # for循环获取每一页的文本数据
        for j in range(0,len(count1)):
            # 获取每页的数据数
            text1 =[driver.find_elements_by_class_name("c-title")[j].text]
            print(text1)
            text2=[driver.find_elements_by_class_name("c-title-author")[j].text]
            print(text2)
            data.append([text1,text2])

            file_path = 'D:\\数据集\\'+keyword+'.xlsx'
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
        try:
            driver.find_element_by_link_text("下一页>").click()
            time.sleep(2)
        except Exception:
            pass
    # 关闭浏览器
    driver.close()
#调用函数
keywords = ['js', 'linux']
for word in keywords:
    get_Search(word)
    time.sleep(3)
