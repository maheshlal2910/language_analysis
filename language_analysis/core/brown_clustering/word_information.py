def bigrams(text):
    text_list = text.split()
    return [(text_list[i-1], text_list[i])for i in range(1, len(text_list))]

def find_merger_candidate(cluster, among):
    pass
