import nltk
from nltk.corpus import brown

def hedge(Text, interval, wordToInsert):
    i = 0
    wordCount = 0
    newText = list(Text)
    for word in newText:
        if wordCount == interval:
            newText.insert(i, wordToInsert)
            wordCount = -1
        if newText[i].isalpha():
            wordCount +=1
        i += 1
    return newText

emma = nltk.corpus.gutenberg.words('austen-emma.txt')

emma = hedge(emma, 3, 'like')

print(emma[:10])

# import nltk
# from nltk.corpus import brown

# def hedge(text):
#     index = 0
#     textList = list(text)
    
#     for word in text:
#         index += 1
#         if (index % 3 == 0) and (index >= 3):
#             textList.insert(index - 1, 'like')
    
#     return textList

# emma = nltk.corpus.gutenberg.words('austen-emma.txt')
# print(hedge(emma)[len(hedge(emma))-10:])