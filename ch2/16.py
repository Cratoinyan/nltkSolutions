import nltk
from nltk.corpus import brown

def lexicalDiversity(text):
    return len(set(word.lower() for word in text if word.isalpha())) / len([word for word in text if word.isalpha()])

lexicalDiversityDic = {}

for genre in brown.categories():
    lexicalDiversityDic[genre] = lexicalDiversity(brown.words(categories=genre))
    print('Lexical Diversity of ' + genre + ' : ' + str(lexicalDiversityDic[genre]))