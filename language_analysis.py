from py2neo import Graph
from functools import partial
from uuid import uuid1

from language_analysis.core.clean.cleaner import clean as doc_cleaner
from language_analysis.core.matricizer.matrix import Matrix
from language_analysis.core.brown_clustering.word_information import *
from language_analysis.neo4j.documents import *
from language_analysis.neo4j.mapper import create_corpus_from
from language_analysis.neo4j.commons import get_batch_of_nodes_to_process

graph = Graph()

doc_repo = UnprocessedDocumentsRepository(graph)
processed_doc_repo = ProcessedDocumentRepository(graph)
word_repo = WordRepository(graph)
cluster_repo = Cluster_repository(graph)
node_fetcher = partial(get_batch_of_nodes_to_process, node_fetcher=doc_repo.get_unprocessed_docs)
word_fetcher = partial(get_batch_of_nodes_to_process, node_fetcher = word_repo.fetch_words)
all_bigrams = []

def extract_words_into_single_clusters(node_fetcher):
    for nodes in node_fetcher():
        corpus = create_corpus_from(nodes)
        corpus.clean_using(doc_cleaner)
        mat = Matrix()
        df_values = mat.create_tf_df_values(corpus)
        word_repo.save_words(df_values)
        processed_doc_repo.save_processed_documents(corpus)


def merge_clusters(level):
    all_clusters = word_repo.words_at_cluster_level(level)
    half_the_clusters = all_clusters[1:int(len(all_clusters)/2)]
    cluster_tuples = [(cluster,find_merger_candidate(cluster, among = all_clusters)) for cluster in half_the_clusters]
    # map(merge, to_be_merged_cluster_pairs)

def create_level0_clusters(words):
    [cluster_repo.assign_word_to_cluster(word, cluster_repo.create(0)) for word in words]

for word_nodes in word_fetcher():
    create_level0_clusters([word.properties['name'] for word in word_nodes])
