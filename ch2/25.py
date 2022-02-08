import re
import nltk
from nltk.corpus import udhr


def find_language(word, encoding):
    langs = [lang for lang in udhr.fileids() if lang.endswith(encoding)]
    langsToReturn = []
    for lang in langs:
        if word in udhr.words(lang):
            langsToReturn.append(lang)
    return langsToReturn

print(find_language('is','-Latin1'))