from language_analysis.core.model import *


def create_document_from(node):
    return Document(node.properties["_id"], node.properties["cleanedText"])


def create_corpus_from(nodes):
    return Corpus([create_document_from(node) for node in nodes])
