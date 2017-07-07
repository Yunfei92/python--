import re
import numpy as np
import collections as col


# 正序输出文本
def Positive_order(avg_feq):
    print('__________Positive-order text_________')
    print('**************************************')
    a = np.argsort(avg_feq)  # 返回正序排序后相对应的索引值
    for n in a:
        print(lines[n])


# 逆序输出文本
def Reverse_order(avg_feq):
    print('__________Reverse-order text_________')
    print('**************************************')
    a = np.argsort(-avg_feq)  # 返回逆序排序后相对应的索引值
    for n in a:
        print(lines[n])


# 计算平均词频
def Cal_avgFreq(lines, words):
    tb = col.Counter(words)  # 计算词频，返回一个字典
    avg_feq = np.zeros(len(lines), dtype=int)  # 初始化一个矩阵，矩阵中的元素都是0，个数是句子的个数
    for n in range(len(lines)):
        s = 0
        line_words = re.split(r'\W+', lines[n])
        line_words = remove_Stopwords(line_words, stop_words)#去掉停止词
        for word in line_words:
            if len(word) > 0:
                word_feq = tb[word.lower()]
                s = s + word_feq  # 计算每一个句子的总词频
        if len(line_words) >0:
            avg_feq[n] = s / len(line_words)  # 计算句子的平均词频
            print(avg_feq[n], lines[n])

    # Positive_order(avg_feq)
    Reverse_order(avg_feq)

#计算平均词长
def cal_avgLength(line, words):
    avg_length = np.zeros(len(lines), dtype=int)  # 初始化一个矩阵，矩阵中的元素都是0，个数是句子的个数
    for n in range(len(lines)):
        s = 0
        line_words = re.split(r'\W+', lines[n])
        line_words = remove_Stopwords(line_words,stop_words)

        for word in line_words:
            if len(word) > 0:
                s = s + len(word)  # 计算每一个句子的总词长
        if len(line_words) > 0:
            if n!=0:
                avg_length[n] = s / (len(line_words)-1)  # 计算句子的平均词长
            else:
                avg_length[n] = s / len(line_words)
            print(s,len(line_words),avg_length[n], lines[n])
    Positive_order(avg_length)
    Reverse_order(avg_length)

#删除停用词
def remove_Stopwords(words,stop_words):
    reserved_list=[word for word in words if word not in stop_words]
    return reserved_list




f = open(r'.\document classification.txt', 'r', encoding='utf8')
raw = f.read()
f.close()
stop_words_file=open(r'.\stopwords.docx', 'r', encoding='utf8')
stop_list=stop_words_file.read()
stop_words_file.close()


#导入停止词
stop_words=stop_list.split('\n')


# 将文本分裂成句子和单词
lines = raw.split('.')
lines = lines[:-1]
words = re.split(r'\W+', raw)
words = [word.lower() for word in words]

Cal_avgFreq(lines, words)
#cal_avgLength(lines, words)
