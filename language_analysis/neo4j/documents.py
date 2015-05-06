class UnprocessedDocumentsRepository:

    def __init__(self, graph):
        self.g = graph

    def get_unprocessed_docs(self, skip, limit):
        return self.g.cypher.execute("MATCH (doc:UnprocessedText) RETURN doc SKIP {s} LIMIT {l}", {"s": skip, "l": limit}).to_subgraph().nodes
