import nltk
import collections as col

#定义函数
def count_Words(word):

    counts = col.Counter(word)  # 计算词频
    #转化为字典
    dict1 = dict(counts)
    #实现字典按值大小排序
    dict2=sorted(a.items(),key=lambda e:e[1],reverse=True)

    # 写入文件
    f = open(r'D:\词频统计.txt', 'a', encoding='utf-8')
    for (x,y) in dict2:
        x=str(x)
        x=x+' '+str(y)
        f.write(x + '\n')
    f.close()
 # 读取txt文件
text = open('h:/文章.txt', 'r').read()

#将文本按词取出放入列表
words=nltk.word_tokenize(text)
#定义标点符号集
w=list('\t\().,?[]!;|')+['--']
#过滤掉标点符号
word=[i for i in words if i not in w]

#回调函数
if __name__ == '__main__':
    count_Words(word)