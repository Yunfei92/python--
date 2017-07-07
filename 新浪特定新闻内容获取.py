import requests
import re
from bs4 import BeautifulSoup
global contents
global titles
global pattern
global m
global data_list
def get_Title(url):
    res=requests.get(url)
    a=[]
    #编码格式
    res.encoding='utf-8'
    #使用剖析器为lxml
    soup=BeautifulSoup(res.text,'lxml')
    for news in soup.select('.news-item'):
        h2 = news.select('h2')
        # 只选择长度大于0的结果
        if len(h2) > 0:
            # 新闻时间
            time = news.select('.time')[0].text
            # 新闻标题
            title = h2[0].text
            # 新闻链接
            href = h2[0].select('a')[0]['href']
            # 打印
        data={'time':time,'title':title,'href':href}
        #print(data['href'])
        pattern = re.compile(r'.*香港警署.*')
        m=re.search(pattern, data['title'])
        # print(m)
        if m:
           url=data['href']
           a.append(url)
    return a
def get_Content(url):
    res = requests.get(url)
    # 编码格式
    res.encoding = 'utf-8'
    # 使用剖析器为lxml
    soup = BeautifulSoup(res.text, 'lxml')
    contents = soup.select('.left p ')
    for content in contents:
        # 写入文件
        f = open(r'D:\新浪新闻特定内容爬取.txt', 'a',encoding='utf-8')
        f.write(content.get_text() + '\n')
        f.close()
#调用函数
a=get_Title('http://news.sina.com.cn/china/')
print(a)
for i in a:
    get_Content(i)


