import nltk
from nltk.corpus import wordnet as wn

def avarage_hyponym():
    synsets = wn.all_synsets('n')
    synsetNumber = 0
    hyponymNumber = 0

    for synset in synsets:
        if synset.hyponyms() != []:
            hyponymNumber += len(synset.hyponyms())
            synsetNumber += 1
    
    return hyponymNumber/synsetNumber

print(avarage_hyponym())