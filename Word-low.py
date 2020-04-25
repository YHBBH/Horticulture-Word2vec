# from numba import jit
# import numpy as np
# import time
# #利用jit编译加速 cpu
# @jit
# def my_add(a,b):
#     return a+b

# def my_numba_add(x, y):
#     return x + y

# def test(n):
#     a = np.array((n))
#     b = np.array((n))
#     tic1 = time.time()
#     my_add(a, b)
#     t1 = time.time() - tic1
#     print('python time:', t1)
#
#     tic2 = time.time()
#     my_numba_add(a, b)
#     t2 = time.time() - tic2
#     print('Numba time:', t2)
#     print('Numba acclerated %f times' % (t1 / t2))
#
# if __name__ == "__main__":
#
#     test(1000)

import re
#判断大小写
# print('one-pot'.isupper())
list1 = []
# with open(r'F:/学习/命名实体/Word2vect/new-test/TOKEN-dic.txt', encoding='utf-8') as f:
#     for line in f.readlines():
#         words = line.split(' ')
#
#         for word in words:
#             # print(word)
#             if word.isupper():
#                 list1.append(word)
#
#             else:
#                 w = word.lower()
#                 list1.append(w)
#
#
#
# with open(r'F:/学习/命名实体/Word2vect/new-test/TOKEN-dicLOW.txt', 'a+', encoding='utf-8') as f:
#     for word in list1:
#         f.write(word+' ')

#大写转换为小写
with open(r'F:/学习/命名实体/Word2vect/plant.txt', encoding='utf-8') as f:
    for line in f.readlines():
        words = line.split(' ')

        for word in words:
            w = word.lower()
            list1.append(w)

with open(r'F:/学习/命名实体/Word2vect/plant-low.txt', 'a+', encoding='utf-8') as f:
    for word in list1:
        f.write(word+' ')