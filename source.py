import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import state_union as su
from nltk.corpus import names
from nltk.corpus import gutenberg
from nltk.corpus import genesis

from nltk.corpus import inaugural
from nltk.probability import FreqDist
# cfd = nltk.ConditionalFreqDist(
#         (target, fileid[:4])
#         for fileid in su.fileids()
#         for w in su.words(fileid)
#         for target in ['men', 'women', 'people']
#         if w.lower().startswith(target))

# cfd.plot()
# cfd = nltk.ConditionalFreqDist(
#        (fileid, name[0])
#        for fileid in names.fileids()
#        for name in names.words(fileid))

# cfd.plot()

# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# days = ['i', 'you', 'he', 'she', 'it', 'they']

# cfd = nltk.ConditionalFreqDist(
#     (genre, target)
#     for genre in genres
#     for word in brown.words(categories=genre)
#     for target in days
#     if word.lower().startswith(target))

# cfd.plot()

# austen = nltk.corpus.gutenberg.words('austen-emma.txt')  
# genesis = nltk.corpus.genesis.words('english-kjv.txt')

# num_chars = len([w for w in nltk.text(austen) if w.isalpha()])
# num_words = len([w for w in austen if w.isalpha()])
# num_sents = len(gutenberg.sents('austen-emma.txt'))
# num_vocab = len(set(w.lower() for w in gutenberg.words('austen-emma.txt') if w.isalpha()))
# print("Average number of characters per word:", round(num_chars/num_words))
# print("Average number of words per sent:",  round(num_words/num_sents))
# print("Lexical diversity: {:.5f}".format(num_vocab/num_words))
# print("Total tokens: {:,}".format(num_words))
# print("Total word types: {:,}".format(num_vocab))

# print('--------------------------------')

# num_chars = len([w for w in nltk.text(genesis) if w.isalpha()])
# num_words = len([w for w in genesis if w.isalpha()])
# num_sents = len(nltk.corpus.genesis.sents('english-kjv.txt'))
# num_vocab = len(set(w.lower() for w in genesis if w.isalpha()))
# print("Average number of characters per word:", round(num_chars/num_words))
# print("Average number of words per sent:",  round(num_words/num_sents))
# print("Lexical diversity: {:.5f}".format(num_vocab/num_words))
# print("Total tokens: {:,}".format(num_words))
# print("Total word types: {:,}".format(num_vocab))



# count words in the dictionary that have more than one possible pronunciation
# iterate over the dict and find those whose values' length is greater than 1

# def supergloss(s):
#     superDef = str(s.definition())
#     hyponyms = s.hyponyms()
#     hypernyms = s.hypernyms()
#     for hypernym in hypernyms:
#         superDef += hypernym.definition() + '\n'
#     for hyponym in hyponyms:
#         superDef += hyponym.definition() + '\n'
#     return superDef


# print(supergloss(wn.synset('car.n.01')))

fdist = FreqDist(word.lower() for word in brown.words())
moreThanThree = [word for word in fdist if fdist[word] >= 3]
print(len(moreThanThree))
