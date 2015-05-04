from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from functools import reduce
import re

from language_analysis.core.clean.custom_stemmer import stemmer

class PunctuationCleaner:

    punctuations = frozenset(["'", "!", ",", '"', "?", ":", "(", ")", "{", "}", "[", "]", "+", "-", "*", "/", "$", "@", "#", "^", "&", "|", "\\", "."])

    def clean(self, doc):
        for punctuation in self.punctuations:
            doc = doc.replace(punctuation, " ")
        doc = doc.strip()
        doc = re.sub(r'\s+', ' ', doc)
        return doc


class StopwordCleaner:

    stopwords_list = frozenset(stopwords.words('english'))

    def clean(self, doc):
        word_list = doc.split()
        return " ".join([word for word in word_list if(word not in self.stopwords_list)])


punctuation_cleaner = PunctuationCleaner()

stopword_cleaner = StopwordCleaner()

def clean(doc):
    cleaned_doc = stopword_cleaner.clean(punctuation_cleaner.clean(doc.lower()))
    stemmed_doc = " ".join([stemmer.stem(word) for word in cleaned_doc.split()])
    return stemmed_doc
