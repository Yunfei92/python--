import pymysql
import requests
from bs4 import BeautifulSoup
a=[]
def get_content(url):
    #获取链接
    res=requests.get(url)
    # 设置编码格式
    res.encoding = 'GB2312'
    #使用html.parser剖析器
    soup=BeautifulSoup(res.text,'html.parser')
    #获取新闻标题列表
    titles=soup.select('a.anavy')
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', password='123456', database='news',charset='utf8')
    # 使用cursor()方法创建一个游标对象 cursor
    cursor = db.cursor()
    for title in titles:
         a=title.get_text()
         b=title['href']
        # print(b)
        # 执行sql语句
         cursor.execute('INSERT INTO DATA VALUES ("%s","%s")' %(db.escape_string(a),db.escape_string(b)))
        # 提交到数据库执行
         db.commit()
    db.close()
    # for i in range(len(titles)):
    #     title = (titles[i])
    #     datas = [title.get_text(), title['href']]
    #     a.append(datas)
    # print(a)

#使用execute()方法执行sql语句,如果存在则删除
# cursor.execute('DROP TABLE IF EXISTS DATA ')
# #使用预处理语句创建表
# sql = """CREATE TABLE DATA (
#           TITLE  CHAR(50) NOT NULL,
#           HREF CHAR(100) )"""
#使用预处理语句向数据库表中插入数据
     # for i in a:

#查询数据库表中所有的数据
# sql="SELECT * FROM EMPLOYEE WHERE INCOME >'%d'" % (1000)
# try:
#     #执行sql语句
#     cursor.execute(sql)
#     #获取所有记录列表
#     results=cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" %
#               (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fecth data")
#
#     #提交到数据库执行
#     # db.commit()
# # except:
# #     #如果发生错误就回滚
# #     db.rollback()
# 关闭数据库连接
get_content('http://news.people.com.cn/GB/124658/index.html')