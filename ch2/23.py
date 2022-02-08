#this code hase been taken from https://github.com/HaelChan because i don't know matplotlib and plotting graphs
import nltk
import random
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.corpus import brown

def max_of_list(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max

def zipfs_law(text):
    fdist = FreqDist([w.lower() for w in text if w.isalpha()])
    fdist = fdist.most_common()

    rank = []
    freq = []
    n = 1
    
    for i in range(len(fdist)):
        freq.append(fdist[i][1])

        rank.append(n)
        n += 1

    plt.plot(rank, freq, 'bs')
    plt.xscale('log')
    plt.title("Zipf's law")
    plt.xlabel('word rank')
    plt.ylabel('word frequency')
    plt.show()

def random_text():
    words = list(set([word.lower() for word in brown.words() if word.isalpha()]))
    sent = ''
    for i in range(1000000):
        sent += random.choice(words) + ' '
    return sent
    

sent = random_text()
print(sent[:100])

zipfs_law(sent.split())

# import matplotlib as plt
# from nltk.probability import FreqDist
# from nltk.corpus import brown

# def zipf_law(text):
#     fdist = FreqDist([w.lower() for w in text if w.isalpha()])
#     fdist.most_common()

#     rankList = []
#     freqList = []
#     rank = 1

#     for i in range(len(fdist)):
#         freqList.append(fdist[i][1])
#         rankList.append(rank)
#         rank += 1
    
#     plt.plot(rankList, freqList, 'bs')
#     plt.xscale('log')
#     plt.title("Zipf's Law")
#     plt.xlabel('Word Rank')
#     plt.ylabel('Word Frequency')
#     plt.show()

# zipf_law(brown.words())