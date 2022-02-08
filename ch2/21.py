import nltk
from nltk.corpus import cmudict

def amountOfSyllableEst(text):
    syllableNumber = 0
    prondict = cmudict.dict()

    for word in text:
        if word.lower() in prondict.keys():
            syllableNumber += len(prondict[word.lower()][0])
    return syllableNumber

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(amountOfSyllableEst(emma))