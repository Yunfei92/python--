import re
import urllib.parse
import urllib.request




def translate(text):
    '''''模拟浏览器的行为，向Google Translate的主页发送数据，然后抓取翻译结果 '''

    # text 输入要翻译的英文句子
    text_1 = text
    # 'langpair':'en'|'zh-CN'从英语到简体中文
    values = {'hl': 'zh-CN', 'ie': 'UTF-8', 'text': text_1, 'langpair': "'en'|'zh-CN'"}
    url = 'http://translate.google.cn/translate_t'
    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, data)
    # 模拟一个浏览器
    browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
    req.addheaders = [
        ('User-Agent',  browser)
    ]
    # 向谷歌翻译发送请求
    response =urllib.request.Request(req)
    # 读取返回页面
    html = response.read()
    # 从返回页面中过滤出翻译后的文本
    # 使用正则表达式匹配
    # 翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
    # .*? non-greedy or minimal fashion
    # (?<=...)Matches if the current position in the string is preceded
    # by a match for ... that ends at the current position
    p = re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
    m = p.search(html)
    text_2 = m.group(0).strip(';')
    return text_2


if __name__ == "__main__":
    # text_1 原文
    # text_1=open('c:\\text.txt','r').read()
    text_1 = 'Hello, my name is Derek. Nice to meet you! '
    print('The input text: %s' % text_1)
    text_2 = translate(text_1).strip("'")
    print('The output text: %s' % text_2)

    # 保存结果
    filename = 'c:\\Translation.txt'
    fp = open(filename, 'w')
    fp.write(text_2)
    fp.close()

    report = 'Master, I have done the work and saved the translation at ' + filename + '.'
    print('Report: %s' % report)  