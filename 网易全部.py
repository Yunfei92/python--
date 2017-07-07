import requests
import re
from bs4 import BeautifulSoup
global contents
global titles
global pattern
global m
global title
global title1
def get_Title(url):
    res=requests.get(url)
    a=[]
    #编码格式
    res.encoding='gbk'
    #使用剖析器为lxml
    soup=BeautifulSoup(res.text,'lxml')
    # print(soup)
    # 获取新闻标题列表
    titles = soup.select('.area.areabg1 tr td a')
    #print(titles)
    for i in range(len(titles)):
        title = (titles[i])
        #print(title.get_text())
        data = {'title':title.get_text(), 'href':title['href']}
        #print(data)
        pattern = re.compile(r'.*共享单车.*')
        m=re.search(pattern, data['title'])
        # print(m)
        if m:
           title1=data['title']
           url=data['href']
           a.append(title1)
           a.append(url)
    #print(a)
    return a
def get_Title1(text):
        f = open(r'D:\网易新闻排行榜全部特定内容爬取.txt', 'a', encoding='utf-8')
        f.write(text + '\n')
        f.close()
def get_Content(url):
    res = requests.get(url)
    # 编码格式
    res.encoding = 'gbk'
    # 使用剖析器为lxml
    soup = BeautifulSoup(res.text, 'lxml')
    content1 = soup.select('.post_text p ')
    for content in contents:
        # 写入文件
        f = open(r'D:\网易新闻排行榜全部特定内容爬取.txt', 'a',encoding='utf-8')
        f.write(content.get_text() + '\n')
        f.close()
#调用函数
a=get_Title('http://news.163.com/rank/')
print(a)
print(a[1])
# for i in range(0,3,2):
#     get_Title1(a[i])
#     for i in range(1,4,2):
#         get_Content(a[i])
get_Title1(a[0])
get_Content(a[1])
# get_Title1(a[2])
# get_Content(a[3])
# get_Title1(a[4])
# get_Content(a[5])