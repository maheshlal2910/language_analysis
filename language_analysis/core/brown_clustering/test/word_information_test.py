import unittest

from language_analysis.core.brown_clustering.word_information import *

class BigramsText(unittest.TestCase):

    def setUp(self):
        pass

    def test_should_give_all_bigrams_for_text(self):
        all_bigrams = bigrams("quick brown fox jumps over")
        assert all_bigrams == [("quick", "brown"), ("brown","fox"), ("fox","jumps"), ("jumps","over")]