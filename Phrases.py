from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, Phraser


# Load training data.
sentences = Text8Corpus(datapath(r'F:/学习/命名实体/Word2vect/new-test/TOKEN-diclow.txt'))
# The training corpus must be a sequence (stream, generator) of sentences,
# with each sentence a list of tokens:
# print(list(sentences)[0][:10])


# Train a toy bigram model.
phrases = Phrases(sentences, min_count=15, threshold=5, max_vocab_size=40000000, delimiter=b'-')
# Apply the trained phrases model to a new, unseen sentence.
bigram = Phraser(phrases)

print(list(sentences)[1])
for i in range(len(list(sentences))):
    # i = int(i)
    sent = phrases[list(sentences)[i][:]]
    s = bigram[sent]
    # print(sentences)
    # print(s)
    # print(bigram[sent])


    with open(r'F:/学习/命名实体/Word2vect/new-test/TOKEN-diclow-phr.txt', 'a+', encoding='utf-8') as f:
        for i in s:

            f.writelines(i+' ')
