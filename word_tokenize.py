
import nltk
from nltk.tokenize import MWETokenizer

list = []
# text = "Horticulture Theory Life in spite of vegetable lan at the cucumis sativas L. riparian Michurin Theory forest Survey on nature environment Cucumber mosaic virus "
# text1 = nltk.word_tokenize(text)
# print(text1)
with open(r'F:/学习/命名实体/Word2vect/new-test/TOKEN-diclow.txt', 'r+', encoding='utf-8') as f:
    text = f.read()

with open(r'F:/学习/命名实体/Word2vect/plant-low.txt', encoding='utf-8') as f:
    words = f.read().splitlines()
    print(words)
    for word in words:
        word = word.split(' ')
        word = tuple(word)
        list.append(word)
    print(list)
    tokenizer = MWETokenizer(list, separator='-')
    # tokenizer.add_mwe(('in', 'spite', 'of'))
    text2 = tokenizer.tokenize(nltk.word_tokenize(text))
# print(list[1])
# print(text2)

with open(r'F:/学习/命名实体/Word2vect/new-test/plant-dict.txt', 'a+', encoding='utf-8') as f:
    for i in text2:
        f.writelines(i+' ')

