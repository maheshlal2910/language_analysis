from functools import reduce, partial
from numpy import log


class WordFrequency:
    def __init__(self):
        pass

    def formulate_word_freq_list(self, doc):
        self.freq_distribution = {}
        doc_words = doc.word_list()
        [self.__increase_count(word) for word in doc_words]
        frequency = partial(self.__calculate_frequency_for, count_of_words=len(doc_words))
        [frequency(word) for word in self.freq_distribution.keys()]
        return self.freq_distribution


    def __calculate_frequency_for(self, word, count_of_words=0):
        self.freq_distribution[word] = log(1 + (self.freq_distribution[word] / count_of_words))


    def __increase_count(self, word):
        if (self.freq_distribution.get(word)):
            self.freq_distribution[word] = self.freq_distribution.get(word) + 1
        else:
            self.freq_distribution[word] = 1


def increment_doc_frequency(accumulator, doc, w=""):
    if w in doc.bag_of_words():
        accumulator += 1
    return accumulator


def document_frequency(word, corpus):
    x = partial(increment_doc_frequency, w=word)
    return reduce(x, corpus.docs, 0)


class Matrix:
    def __init__(self):
        pass

    def create_tf_df_values(self, corpus):
        word_frequency_calculator = WordFrequency()
        docs_with_term_frequencies = [doc.compose(word_frequency_calculator.formulate_word_freq_list(doc)) for doc in
                                      corpus.docs]
        corpus.replace_docs_with(docs_with_term_frequencies)
        bag_of_words = reduce(set.union, [doc.bag_of_words() for doc in corpus.docs], set())
        doc_frequency_distribution = {word: document_frequency(word, corpus) for word in bag_of_words}
        return doc_frequency_distribution
