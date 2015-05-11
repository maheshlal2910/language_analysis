from py2neo import Graph
from functools import partial

from language_analysis.core.clean.cleaner import clean as doc_cleaner
from language_analysis.core.matricizer.matrix import Matrix
from language_analysis.neo4j.documents import *
from language_analysis.neo4j.mapper import create_corpus_from
from language_analysis.neo4j.commons import get_batch_of_nodes_to_process

graph = Graph()

doc_repo = UnprocessedDocumentsRepository(graph)
processed_doc_repo = ProcessedDocumentRepository(graph)
word_repo = WordRepository(graph)
node_fetcher = partial(get_batch_of_nodes_to_process, node_fetcher=doc_repo.get_unprocessed_docs)


# def process(corpus):
#     mat = Matrix()
#     mat.create_tf_df_values(corpus)


for nodes in node_fetcher():
    corpus = create_corpus_from(nodes)
    corpus.clean_using(doc_cleaner)
    mat = Matrix()
    df_values = mat.create_tf_df_values(corpus)
    word_repo.save_words(df_values)
    processed_doc_repo.save_processed_documents(corpus)
