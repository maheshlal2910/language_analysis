def get_batch_of_nodes_to_process(node_fetcher, step=10):
    skip = 0
    limit = step
    nodes = node_fetcher(skip, limit)
    while nodes:
        if nodes:
            yield nodes
        else:
            raise StopIteration()
        skip += step
        nodes = node_fetcher(skip, limit)
