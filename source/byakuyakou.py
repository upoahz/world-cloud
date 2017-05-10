# coding=utf-8
import jieba.analyse

path = '/Users/zhao/workspace/zpnotes/world-cloud/data/byakuyakou.txt'

with open(path, 'r', encoding='utf-8') as f:
    data = f.read()

try:
    jieba.analyse.set_stop_words('/Users/zhao/workspace/zpnotes/world-cloud/data/stopwords.dat')
    tags = jieba.analyse.extract_tags(data, topK=100, withWeight=True)
    for v, n in tags:
        print(v + '\t' + str(int(n * 10000)))
finally:
    f.close()