from uuid import uuid1


class UnprocessedDocumentsRepository:

    def __init__(self, graph):
        self.g = graph

    def get_unprocessed_docs(self, skip, limit):
        return self.g.cypher.execute("MATCH (doc:UnprocessedText) RETURN doc SKIP {s} LIMIT {l}", {"s": skip, "l": limit}).to_subgraph().nodes


class ProcessedDocumentRepository:

    def __init__(self, graph):
        self.g = graph

    def save_processed_documents(self, corpus):
        merge_cypher = "MATCH  (doc:UnprocessedText{_id:{doc_id}}), (w:Word{name:{word_name}}) MERGE (doc)-[r:HAS_WORD]->(w) ON CREATE SET r.term_frequency = {tf} ON MATCH SET r.term_frequency = {tf}"
        [self.g.cypher.execute(merge_cypher, {'word_name': word, 'doc_id': document._id, 'tf':document.term_frequencies[word] }) for document in corpus.docs for word in document.term_frequencies.keys()]


class WordRepository:

    def __init__(self, graph):
        self.g = graph

    def save_words(self, doc_frequencies):
        merge_cypher = "MERGE (w:Word{name:{word_name}}) ON CREATE SET w.doc_freq={df} ON MATCH SET w.doc_freq={df}"
        [self.g.cypher.execute(merge_cypher, {'word_name': word, 'df': doc_frequencies[word]}) for word in doc_frequencies.keys()]

    def words_at_cluster_level(self, level):
        self.g.cypher.execute("MATCH (c:Cluster{level:})")

    def fetch_words(self, skip, limit):
        return self.g.cypher.execute("MATCH (word:Word) RETURN word SKIP {s} LIMIT {l}", {"s": skip, "l": limit}).to_subgraph().nodes


class Cluster_repository:

    def __init__(self, graph):
        self.g = graph

    def assign_word_to_cluster(self, word, cluster_id):
        self.g.cypher.execute("MATCH (c:Cluster{_id:{cluster_id}}), (w:Word{name:{word}}) CREATE (w)-[:BELONGS_TO]->(c)", {'word': word, 'cluster_id': cluster_id})

    def create(self, level):
        cluster_id = str(uuid1())
        self.g.cypher.execute("CREATE (c:Cluster{_id:{cluster_id}, level:{level}})", {'level':level, 'cluster_id': cluster_id})
        return cluster_id
