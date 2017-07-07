import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from urllib import urlopen
import urllib
from bs4 import BeautifulSoup

#网易新闻排行榜
url="http://news.163.com/rank/"
html = urlopen(url)
html = html.read().decode('GB2312','ignore').encode('UTF-8')
bsObj = BeautifulSoup(html,'html.parser')
nameList = bsObj.findAll("td", {"class":"red"})
print nameList
for name in nameList:
    f = open(r'D:\test.txt','a') 
    f.write(name.get_text())
    f.close()