#合并TXT文件
# with open(r'F:/学习/命名实体/Word2vect/DATA/split/AB1.txt', 'r+', encoding='utf-8') as f:
#     for line in f.readlines():
#         s = line
#
#         with open(r'F:/学习/命名实体/Word2vect/DATA/AB-new.txt', 'a+', encoding='utf-8') as f:
#             f.write(s)



#合并文件夹下文档

import os
import os.path

filedir = 'F:/学习/命名实体/资料/cucudata-dev'

filenames=os.listdir(filedir)

f = open('F:/学习/命名实体/资料/devdata.txt', 'w')

for filename in filenames:
    filepath = filedir+'/'+filename

    for line in open(filepath):
        f.writelines(line)
    f.write('\n')

f.close()