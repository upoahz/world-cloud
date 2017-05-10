# coding=utf-8
import os
import jieba.analyse

dirpath = os.path.realpath('../data/keigo-higashino/')
list = os.listdir(dirpath)

for name in list:
    path = dirpath + '/' + name

    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()

    try:
        jieba.analyse.set_stop_words('/Users/zhao/workspace/zpnotes/world-cloud/data/stopwords.dat')
        tags = jieba.analyse.extract_tags(data, topK=100, withWeight=True)
        print('========================================')
        print(name)
        print('========================================')
        for v, n in tags:
            print(v + '\t' + str(int(n * 10000)))
    finally:
        f.close()
