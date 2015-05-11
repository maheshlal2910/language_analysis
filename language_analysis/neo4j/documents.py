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
