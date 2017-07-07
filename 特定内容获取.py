import requests
import re
from bs4 import BeautifulSoup
global contents
global titles
global pattern
global m
global href
def get_Title(url):
    res=requests.get(url)
    #编码格式
    res.encoding='gb2312'
    #使用剖析器为lxml
    soup=BeautifulSoup(res.text,'lxml')
    #获取新闻标题列表
    titles=soup.select('.red a')
    # print(titles)
    for i in range(len(titles)):
        hrefs=soup.select('.red a')[i]['href']
        print(hrefs)
    #获取新闻链接列表
    # p= re.compile(r"<a.*?href=.*?<\/a>")
    # print(p.findall(titles))
    # for i in range(20):
    #     hrefs = soup.select('.tab_01 h3 a')[i]['href']
    #     # print(hrefs)
    # for title,href in zip(titles,hrefs):
    #     data={'title':title.get_text(),'href':hrefs}
    #     print(data)
    # pattern=re.compile(r'.*火箭.*')
    # for title in titles:
    #     m = re.search(pattern,title.get_text())
    #     print(m)


    # 写入文件
    #     f = open(r'D:\文章内容爬取.txt', 'a',encoding='utf-8')
    #     f.write(content.get_text() + '\n')
    #     f.close()
get_Title('http://news.163.com/rank/')