# 文本文件必须是utf-8无bom格式
from gensim.models import Word2Vec

def model_vect(f,output_vector_file):
    model = Word2Vec.load(f)
    word_vector_dict = {}
    items1 = model.most_similar('cucumber',topn=5)
    for i, j in items1:
        print(i, j)
    print('-----------------------------')

    items2 = model.most_similar('cucurbit', topn=5)
    for i, j in items2:
        print(i, j)
    print('-----------------------------')

    items3 = model.most_similar('mother', topn=5)
    for i, j in items3:
        print(i, j)
    print('-----------------------------')

    items4 = model.most_similar(['big', 'bigger'],  ['small'], topn=5)
    for i, j in items4:
        print(i, j)
    print("-------------------------")

    items5 = model.most_similar(['girl', 'father'],  ['boy'], topn=5)
    for i, j in items5:
        print(i, j)
    print("-------------------------")

    print(model['cucumber'])

    for word in model.wv.index2word:
        word_vector_dict[word] = list(model[word])

    with open(output_vector_file, 'w+', encoding='utf-8') as f:
        f.write(str(word_vector_dict))


if __name__ == '__main__':
    model_vect('F:/学习/命名实体/Word2vect/new-test-2/CABData.model','F:/学习/命名实体/Word2vect/new-test-2/word_vector.txt')