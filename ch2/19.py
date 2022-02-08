import nltk
from nltk.corpus import brown

def freqOfWordsByBrownCorpusGenres(words):
    fdist = nltk.ConditionalFreqDist(
        (genre, target)
        for genre in brown.categories()
        for word in brown.words(categories = genre)
        for target in words
        if word.lower().startswith(target)
    )

    fdist.tabulate()

words = ['hey', 'hi', 'son', 'gun', 'school', 'democracy']

freqOfWordsByBrownCorpusGenres(words)