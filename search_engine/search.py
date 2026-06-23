import math
from .tokenizer import tokenize


def search(query, inverted_index, total_documents):
    """
    Searches for documents matching the query and ranks them based on TF-IDF scores.

    Args:
        query (str): The search query.
        inverted_index (dict): The inverted index mapping tokens to documents and their counts.
        total_documents (int): The total number of documents in the corpus.

    Returns:
        list: A list of tuples containing document names and their corresponding relevance scores, sorted by score.
    """
    query_tokens = tokenize(query)
    document_score = {}
    for token in query_tokens:
        if token in inverted_index:
            df = len(inverted_index[token])
            idf = math.log((1 + total_documents) / (1 + df)) + 1
            for doc_name in inverted_index[token]:
                tf = 1 + math.log(inverted_index[token][doc_name])
                document_score[doc_name] = document_score.get(doc_name, 0) + tf * idf

    ranked_documents = sorted(document_score.items(), key=lambda x: x[1], reverse=True)
    return ranked_documents[:10]
