import xlwt
import time
import re
import multiprocessing
from selenium import webdriver

data1=[]
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
            text2=[driver.find_elements_by_class_name("c-author")[j].text]
            print(text2)
            data1.append(text1)
        #以搜索关键字命名文件
        file_path =  'D:\\' +keyword + '.xlsx'
        # 新建一个excell文件
        wb = xlwt.Workbook()
        # 创建一个工作薄
        sheet = wb.add_sheet('数据集')  # sheet的名称为test
        row_count = len(data1)
        col_count = len(data1[0])
        for row in range(0, row_count):
            col_count = len(data1[row])
            for col in range(0, col_count):
                sheet.write(row, col, data1[row][col])
        wb.save(file_path)
        driver.find_element_by_link_text("下一页>").click()
        time.sleep(2)
    # 关闭浏览器
    driver.close()
#调用函数
if __name__ == "__main__":
    #自定义的关键字集合
    keywords=['css','python','java']
    #调用pool类获取当前cpu进程
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    #调用pool类的map方法
    pool.map(get_Search, keywords)
    #关闭进程池（pool）
    pool.close()
    #主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。
    pool.join()

