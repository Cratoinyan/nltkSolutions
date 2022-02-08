import nltk
from nltk.corpus import wordnet as wn

def order_by_similarity(pairs):
    result = {}

    for pair in pairs:
        result[pair[0]+'-'+pair[1]] = wn.synset(pair[0]+'.n.'+'1').path_similarity(wn.synset(pair[1] + '.n.'+ '1'))
    
    result = sorted(result.items(),key= lambda x: x[1], reverse=True)
    
    return result

pairs = [["car", "automobile"], 
          ["gem", "jewel"], 
          ["journey", "voyage"], 
          ["boy", "lad"], 
          ["coast", "shore"], 
          ["asylum", "madhouse"], 
          ["magician", "wizard"], 
          ["midday", "noon"], 
          ["furnace", "stove"], 
          ["food", "fruit"], 
          ["bird", "cock"], 
          ["bird", "crane"], 
          ["tool", "implement"], 
          ["brother", "monk"], 
          ["lad", "brother"], 
          ["crane", "implement"], 
          ["journey", "car"], 
          ["monk", "oracle"], 
          ["cemetery", "woodland"], 
          ["food", "rooster"], 
          ["coast", "hill"], 
          ["forest", "graveyard"], 
          ["shore", "woodland"], 
          ["monk", "slave"], 
          ["coast", "forest"], 
          ["lad", "wizard"], 
          ["chord", "smile"], 
          ["glass", "magician"], 
          ["rooster", "voyage"], 
          ["noon", "string"]]

orderedPairs= order_by_similarity(pairs)

for pair in orderedPairs:
    print(pair)