import requests
from bs4 import BeautifulSoup

url = 'http://news.sina.com.cn/china/'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'UTF-8'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')

#遍历每一个class=news-item的节点
for news in soup.select('.news-item'):
    h2 = news.select('h2')
    #只选择长度大于0的结果
    if len(h2) > 0:
        #新闻时间
        time = news.select('.time')[0].text
        #新闻标题
        title = h2[0].text
        #新闻链接
        # href = h2[0].select('a')[0]['href']
        #打印
        print(time, title)