from nltk.corpus import stopwords
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
    punctuation_cleaned = punctuation_cleaner.clean(doc.lower())
    cleaned_doc = stopword_cleaner.clean(punctuation_cleaned)
    stemmed_doc = " ".join([stemmer.stem(word).lower() for word in cleaned_doc.split()])
    return stemmed_doc
