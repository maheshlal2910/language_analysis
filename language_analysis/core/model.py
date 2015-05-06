class Corpus:

    def __init__(self, docs):
        self.docs = docs

    def clean_using(self, cleaner):
        [doc.clean_using(cleaner) for doc in self.docs]

    def replace_docs_with(self, docs):
        self.docs = docs


class Document:

    def __init__(self, _id, _text, processed_text= "", term_frequencies = {}):
        self._id = _id
        self._text = _text
        self._processed_text = _text
        self._term_frequencies = term_frequencies

    def compose(self, term_frequencies):
        return Document(self._id, self._text, self._processed_text, term_frequencies)

    @property
    def term_frequencies(self):
        return self._term_frequencies

    @property
    def processed_text(self):
        return self._processed_text

    def word_list(self):
        return self._text.split()

    def clean_using(self, cleaner):
        self._processed_text = cleaner(self._text)

    def bag_of_words(self):
        return frozenset(self._processed_text.split())
