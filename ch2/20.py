import nltk
from nltk.corpus import brown

def word_freq(word):
    text = [word for word in brown.words(fileids=['cg22']) if word.isalpha]
    return text.count(word) / len(text)

print(word_freq('is'))