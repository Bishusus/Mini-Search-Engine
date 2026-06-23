from .tokenizer import tokenize


def build_inverted_index(documents):
    """
    Builds an inverted index from the provided documents.

    Args:
        documents (dict): A dictionary where keys are document names and values are the document texts.

    Returns:
        dict: An inverted index mapping each token to a dictionary of documents containing the token.
    """
    inverted_index = {}
    for doc_name, data in documents.items():
        tokens = tokenize(data)
        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = dict()
            if doc_name not in inverted_index[token]:
                inverted_index[token][doc_name] = 0
            inverted_index[token][doc_name] += 1
    return inverted_index
