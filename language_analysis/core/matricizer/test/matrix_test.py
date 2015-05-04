import unittest

from language_analysis.core.matricizer.matrix import *

class WordFrequencyTest(unittest.TestCase):

    def setUp(self):
        self.freq_mat = WordFrequency("this is a stupid doc with some stupid text and no meaning to text")

    def test_should_create_frequency_matrix_for_doc(self):
        self.freq_mat.formulate_word_freq_list()
        count = len("this is a stupid doc with some stupid text and no meaning to text".split())
        assert self.freq_mat.freq_distribution["stupid"] == log(1 + 2/count)
        assert self.freq_mat.freq_distribution["meaning"] == log(1 + 1/count)

    def test_should_get_bag_of_words(self):
        assert self.freq_mat.bag_of_words() == frozenset("this is a stupid doc with some stupid text and no meaning to text".split())


class DocFreqTest(unittest.TestCase):

    def setUp(self):
        self.doc_freq = DocFreq("stupid")
        self.docs = [WordFrequency("this is a stupid doc with some stupid text and no meaning to text"), WordFrequency("are you ready for some stupid fun")]

    def test_should_calculate_the_frequency_of_word_in_text_corpus(self):
        self.doc_freq.doc_freq_of_word(self.docs)
        assert self.doc_freq.frequency_in_corpus == 2


class MatrixTest(unittest.TestCase):

    def setUp(self):
        self.docs = ["stupid doc stupid text no meaning text", "hello you ready text based fun finding meaning"]
        self.mat = Matrix()
        self.mat.create_tf_df_values(self.docs)

    def test_should_create_matrix_consisting_of_doc_frequencies(self):
        first_doc = self.mat.doc_vectors[0]
        count = len(first_doc.doc.split())
        expected_vector ={'doc': log(1 + 1/count), 'meaning': log(1 + 1/count), 'no': log(1 + 1/count), 'stupid': log(1 + 2/count), 'text': log(1 + 2/count)}
        assert first_doc.freq_distribution == expected_vector

    def test_should_get_frequency_of_terms(self):
        expected_frequencies = {'based': 1, 'doc': 1, 'finding': 1, 'fun': 1, 'hello': 1 , 'meaning': 2, 'no': 1, 'ready': 1, 'stupid': 1, 'text': 2, 'you': 1}
        found_frequencies = {frequency_value.word: frequency_value.frequency_in_corpus for frequency_value in self.mat.doc_frequency_values}
        assert  found_frequencies == expected_frequencies
