import random
import nltk
from nltk.corpus import brown

lastWord = None

def generate_model(cfdist, word, num=15):
    lastWord = word
    for i in range(num):
        if word == lastWord:
            print(word, end=' ')
            word = cfdist[word].max()
        else:
            print(word, end=' ')
            word = random.choice(list(cfdist[word]))

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
text = brown.words(categories=('news', 'adventure'))
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

generate_model(cfd, 'I', 100)