import requests
from bs4 import BeautifulSoup
global contents
def get_Pages(url):
    res=requests.get(url)
    #编码格式
    res.encoding='utf-8'
    #使用剖析器为lxml
    soup=BeautifulSoup(res.text,'html.parser')
    contents=soup.select('#picTxt p')
    print(contents)
    for content in contents:
    #写入文件
        f = open(r'D:\111.txt', 'a',encoding='utf-8')
        f.write(content.get_text() + '\n')
        f.close()
get_Pages('http://ent.ifeng.com/a/20170422/42912843_0.shtml?_zbs_baidu_dk#p=1')