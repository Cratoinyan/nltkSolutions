import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.util import bigrams

def mostCommonNonStopwordBigrams(text):
    sWords = stopwords.words('english')
    fdist = FreqDist(bigrams(word for word in text if word.lower() not in sWords))
    print(fdist.most_common(50))

mostCommonNonStopwordBigrams(nltk.corpus.gutenberg.words('austen-emma.txt'))