from search_engine import *


def main():
    documents = load_documents("textFiles")
    total_documents = len(documents)

    # Build inverted index
    inverted_index = build_inverted_index(documents)

    # Example search query
    query = input("Enter your search query: ")
    results = search(query, inverted_index, total_documents)

if __name__ == "__main__":
    main()