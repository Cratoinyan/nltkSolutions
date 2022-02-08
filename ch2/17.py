import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def mostCommonNonStopWords(text):
    sWords = stopwords.words('english')
    fdist = FreqDist(word for word in text if word.lower() not in sWords)
    print(fdist.most_common(50))

mostCommonNonStopWords(nltk.corpus.gutenberg.words('austen-emma.txt'))