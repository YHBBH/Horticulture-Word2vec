#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试gensim使用
"""

from gensim.models import word2vec
import logging

# 主程序
def Word_vect(f, save_model):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(f)  # 加载语料
    model = word2vec.Word2Vec(sentences, size=200, sg=1, window=5)  # 训练skip-gram/CBOW模型; 默认window=5

    # 计算两个词的相似度/相关程度
    # y1 = model.similarity("woman", "man")
    # print(u"woman和man的相似度为：", y1)
    # print("--------\n")

    # 计算某个词的相关词列表
    y2 = model.most_similar("cucumber", topn=5)  # 20个最相关的
    print(u"和cucumber最相关的词有：\n")
    for item in y2:
        print(item[0], item[1])
    print("--------\n")

    # 寻找对应关系
    print(' Similar to ..... \n')
    y3 = model.most_similar(['cucumber', 'pumpkin'], ['cucurbit'], topn=5)
    for item in y3:
        print(item[0], item[1])
    print("--------\n")

    y4 = model.most_similar("virus", topn=5)  # 20个最相关的
    print(u"和virus最相关的词有：\n")
    for item in y4:
        print(item[0], item[1])
    print("--------\n")
    # more_examples = ["he his she", "big bigger bad", "going went being"]
    # for example in more_examples:
    #     a, b, x = example.split()
    #     predicted = model.most_similar([x, b], [a])[0][0]
    #     print("'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted))
    # print("--------\n")

    # 寻找不合群的词
    y4 = model.doesnt_match("breakfast cereal dinner lunch".split())
    print(u"不合群的词：", y4)
    print("--------\n")

    # 保存模型，以便重用
    model.save(save_model)
    # 对应的加载方式
    # model_2 = word2vec.Word2Vec.load("text8.model")

    # 以一种C语言可以解析的形式存储词向量
    # model.save_word2vec_format("text8.model.bin", binary=True)
    # 对应的加载方式
    # model_3 = word2vec.Word2Vec.load_word2vec_format("text8.model.bin", binary=True)


if __name__ == "__main__":
    Word_vect('F:/学习/命名实体/Word2vect/DATA/AB-new.txt', r"F:/学习/命名实体/Word2vect/sk-AB-200/CABData.model")
