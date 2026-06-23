import re

STOPWORDS = {
    "the", "is", "a", "an", "and", "to", "of", "in", "on", "for", "this", "that"
}


def tokenize(text):
    """
    Tokenizes the input text into a list of words.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of words extracted from the input text.
    """
    tokens = re.findall(r'\b\w+\b', text.lower())
    return [token for token in tokens if token not in STOPWORDS]
