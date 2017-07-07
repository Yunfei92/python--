import requests
import re
from bs4 import BeautifulSoup
global pattern1
global pattern
global m
global n
def get_Title(url):
    res=requests.get(url)
    a=[]
    #编码格式utf-8
    res.encoding='gb2312'
    #使用剖析器为lxml
    soup=BeautifulSoup(res.text,'lxml')
    # #正则匹配
    pattern = re.compile(r'.*共享单车.*')
    # 获取新闻标题列表
    titles = soup.select('.area.areabg1 tr td a')
    for i in range(len(titles)):
         title=(titles[i])
         data={'title':title.get_text(),'href':title['href']}
         #print(data)
         m=re.search(pattern,data['title'])
         if m:
            url=data['href']
            a.append(url)
    return a

def get_Content(url):
    global pattern1
    res = requests.get(url)
    # 编码格式
    res.encoding = 'gb2312'
    #正则匹配汉字
    pattern1 = re.compile(r'[\u4e00-\u9fa5]')
    # 使用剖析器为lxml
    soup = BeautifulSoup(res.text, 'lxml')
    contents = soup.select('.post_text p')
    for content in contents:
        # print(content.get_text())
        n=re.search(pattern1,content.get_text())
        if n:
            print(content.get_text())
            f = open(r'D:\网易新闻排行榜特定内容爬取.txt', 'a',encoding='utf-8')
            f.write(content.get_text()+'\n')
            f.close()
#调用函数
a=get_Title('http://news.163.com/rank/')
# print(a)
for i in a:
    get_Content(i)



