from functools import reduce, partial
from numpy import log


class WordFrequency:

    def __init__(self, doc):
        self.doc = doc
        self.freq_distribution = {}

    def formulate_word_freq_list(self):
        doc_words = self.doc.split()
        [self.__increase_count(word) for word in doc_words]
        frequency = partial(self.__calculate_frequency_for, count_of_words = len(doc_words))
        [frequency(word) for word in self.freq_distribution.keys()]

    def __calculate_frequency_for(self, word, count_of_words = 0):
        self.freq_distribution[word] = log(1 + self.freq_distribution[word] / count_of_words)


    def __increase_count(self, word):
        if(self.freq_distribution.get(word)):
            self.freq_distribution[word] = self.freq_distribution.get(word) + 1
        else:
            self.freq_distribution[word] = 1

    def bag_of_words(self):
        return frozenset(self.doc.split())


class DocFreq:

    def __init__(self, word):
        self.word = word
        self.frequency_in_corpus = 0

    def doc_freq_of_word(self, docs):
        for doc in docs:
            if(self.word in doc.bag_of_words()):
                self.frequency_in_corpus = self.frequency_in_corpus + 1


class Matrix:

    def __init__(self):
        pass

    def create_tf_df_values(self, corpus):
        self.doc_vectors = [WordFrequency(doc) for doc in corpus]
        [vector.formulate_word_freq_list() for vector in self.doc_vectors]
        bag_of_words = reduce(set.union, [doc_vector.bag_of_words() for doc_vector in self.doc_vectors], set())
        self.doc_frequency_values = [DocFreq(word) for word in bag_of_words]
        [frequency.doc_freq_of_word(self.doc_vectors) for frequency in self.doc_frequency_values]
