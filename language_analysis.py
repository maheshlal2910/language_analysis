from py2neo import Graph

from language_analysis.core.clean.cleaner import clean as doc_cleaner
from language_analysis.core.matricizer.matrix import Matrix
from language_analysis.neo4j.documents import *
from language_analysis.neo4j.mapper import create_corpus_from

graph = Graph()

doc_repo = UnprocessedDocumentsRepository(graph)
# node_fetcher = partial(get_batch_of_nodes_to_process, node_fetcher=doc_repo.get_unprocessed_docs)


def process(corpus):
    mat = Matrix()
    print(mat.create_tf_df_values(corpus))


corpus = create_corpus_from(doc_repo.get_unprocessed_docs(0, 10))
corpus.clean_using(doc_cleaner)
process(corpus)
for doc in corpus.docs:
    print(doc.processed_text)
    print(doc.term_frequencies)
