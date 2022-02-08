import nltk, re, pprint, feedparser, os
from urllib import request
from nltk import word_tokenize
from bs4 import BeautifulSoup

#turn Lord Of The Rings: Fellowship Of The Ring into a corpus from a txt file
# lotrFile = open('ch3/TFOTR.txt')
# rawLotr = lotrFile.read()
# tokens = word_tokenize(rawLotr)
# lotr = nltk.Text(tokens)

# for word in lotr[:80]:
#     print(word, end=' ')
#     if word == ',' or word == '.':
#         print()

#####################################################################################################
#turn Lord Of The Rings: Return Of The King into a corpus from a website

# url = 'https://ae-lib.org.ua/texts-c/tolkien__the_lord_of_the_rings_3__en.htm'
# html = request.urlopen(url).read()
# raw = BeautifulSoup(html, 'html.parser').get_text()
# index = raw.find('Pippin') - 28
# raw = raw[index:]
# lotr = nltk.Text(word_tokenize(raw))

url = 'https://www.nytimes.com/2021/11/09/business/powells-books-pandemic.html'
html = request.urlopen(url).read()
raw = BeautifulSoup(html, 'html.parser').get_text()
news = nltk.Text(word_tokenize(raw))

for word in news[:500]:
    print(word, end=" ")