import unittest

from language_analysis.core.matricizer.matrix import *
from language_analysis.core.model import Corpus, Document

class WordFrequencyTest(unittest.TestCase):

    def setUp(self):
        self.freq_mat = WordFrequency()

    def test_should_create_frequency_matrix_for_doc(self):
        self.freq_mat.formulate_word_freq_list(Document(123, "this is a stupid doc with some stupid text and no meaning to text",
                                                        "this is a stupid doc with some stupid text and no meaning to text"))
        count = len("this is a stupid doc with some stupid text and no meaning to text".split())
        assert self.freq_mat.freq_distribution["stupid"] == log(1 + 2/count)
        assert self.freq_mat.freq_distribution["meaning"] == log(1 + 1/count)


class DocFreqTest(unittest.TestCase):

    def setUp(self):
        self.docs = [Document(123, "stupid doc stupid text no meaning text", "stupid doc stupid text no meaning text"),
                     Document(124,"hello you ready text based fun finding meaning", "hello you ready text based fun finding meaning")]
        self.corpus = Corpus(self.docs)

    def test_should_calculate_the_frequency_of_word_in_text_corpus(self):
        assert document_frequency('stupid', self.corpus) == 1


class MatrixTest(unittest.TestCase):

    def setUp(self):
        self.docs = [Document(123, "stupid doc stupid text no meaning text", "stupid doc stupid text no meaning text"),
                     Document(124,"ready text meaning", "ready text meaning")]
        self.corpus = Corpus(self.docs)
        self.mat = Matrix()
        self.doc_frequency_distribution = self.mat.create_tf_df_values(self.corpus)

    def test_should_create_matrix_consisting_of_doc_frequencies(self):
        first_doc = self.corpus.docs[0]
        count = len(first_doc.processed_text.split())
        expected_vector = {'doc': log(1 + (1/count)), 'meaning': log(1 + (1/count)), 'no': log(1 + (1/count)), 'stupid': log(1 + (2/count)), 'text': log(1 + (2/count))}
        assert first_doc.term_frequencies == expected_vector

    def test_should_get_frequency_of_terms(self):
        expected_frequencies = {'doc': 1, 'meaning': 2, 'no': 1, 'ready': 1, 'stupid': 1, 'text': 2}
        assert self.doc_frequency_distribution == expected_frequencies
