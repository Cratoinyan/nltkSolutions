import nltk
from nltk.corpus import wordnet as wn

# def avarage_polyseyms():
#     dictPolyseym = {}
#     for i in ['n', 'v', 'a', 'r']:
#         numberOfPolyseyms = 0
#         numberOfSynsets = 0
#         lemmas = []
#         for synset in wn.all_synsets(i):
#             for name in synset.lemma_names():
#                 lemmas.append(name)
    
#         for lemma in set(lemmas):
#             numberOfPolyseyms += len(wn.synsets(lemma, i))
#             numberOfSynsets +=1
#         dictPolyseym[i] = numberOfPolyseyms/numberOfSynsets
#     return dictPolyseym

# print(avarage_polyseyms())