import os


def load_documents(folder):
    """
    Loads all text documents from the specified folder.

    Args:
        folder (str): The path to the folder containing text documents.

    Returns:
        dict: A dictionary mapping filenames to file content.
    """
    documents = {}
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                documents[filename] = text
    return documents
