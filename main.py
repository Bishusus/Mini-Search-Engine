from search_engine import *


def main():
    documents = load_documents("textFiles")
    total_documents = len(documents)

    # Build inverted index
    inverted_index = build_inverted_index(documents)

    # Example search query
    query = input("Enter your search query: ")
    results = search(query, inverted_index, total_documents)

    # Display results
    if results:
        print("\nTop 10 relevant documents:")
        for i, (doc_name, score) in enumerate(results, start=1):
            print(f"Rank {i}. {doc_name}: {score:.4f}")
    else:
        print("No relevant documents found.")


if __name__ == "__main__":
    main()