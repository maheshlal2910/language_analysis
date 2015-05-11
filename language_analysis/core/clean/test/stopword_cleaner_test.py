import unittest

from language_analysis.core.clean.cleaner import *

class StopwordCleanerTest(unittest.TestCase):

    def setUp(self):
        self.cleaner = StopwordCleaner()

    def test_should_clean_all_stopwords_present(self):
        cleaned_output = self.cleaner.clean("Hello there this is Sparta")
        expected = "Hello Sparta"
        assert cleaned_output == expected


class PunctuationCleanerTest(unittest.TestCase):

    def setUp(self):
        self.cleaner = PunctuationCleaner()

    def test_should_clean_all_punctuation_present(self):
        cleaned_output = self.cleaner.clean("Hello,there this is:Sparta!")
        expected = "Hello there this is Sparta"
        assert cleaned_output == expected


class CleanerTest(unittest.TestCase):

    def test_cleans_All_punctuations_and_stopwords(self):
        sentence = "Hello,there this is Sparta!"
        cleaned_sentence = clean(sentence)
        assert cleaned_sentence == "hello spart"

