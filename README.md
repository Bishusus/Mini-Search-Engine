# Mini Search Engine 🔍

A lightweight, yet powerful search engine implemented in Python that crawls text files and retrieves the most relevant documents based on your search queries using TF-IDF (Term Frequency-Inverse Document Frequency) scoring.

## Features ✨

- **Fast Indexing**: Builds an inverted index for quick document retrieval
- **TF-IDF Ranking**: Ranks documents by relevance using industry-standard TF-IDF algorithm
- **Stopword Filtering**: Removes common stopwords for better search accuracy
- **Easy to Use**: Simple command-line interface for searching
- **Scalable**: Can handle multiple text documents efficiently
- **Well-Structured**: Modular design with separate components for each functionality

## Architecture 🏗️

The project is organized into modular components:

```
Mini-Search-Engine/
├── main.py                 # Entry point of the application
├── search_engine/          # Core search engine package
│   ├── __init__.py        # Package initialization and exports
│   ├── loader.py          # Document loading from filesystem
│   ├── tokenizer.py       # Text tokenization and stopword removal
│   ├── indexer.py         # Inverted index construction
│   └── search.py          # Query processing and TF-IDF scoring
└── textFiles/             # Sample text documents directory
```

### Module Descriptions

#### `loader.py`
Handles loading all `.txt` files from a specified directory into memory.
- **Function**: `load_documents(folder)` - Loads documents from a folder

#### `tokenizer.py`
Converts text into tokens (words) and removes common stopwords.
- **Function**: `tokenize(text)` - Tokenizes text and filters stopwords
- **Stopwords**: Common words like "the", "is", "and", etc. are automatically filtered out

#### `indexer.py`
Creates an inverted index mapping tokens to documents and their frequencies.
- **Function**: `build_inverted_index(documents)` - Builds the inverted index structure

#### `search.py`
Implements the search algorithm using TF-IDF scoring.
- **Function**: `search(query, inverted_index, total_documents)` - Searches and ranks documents

## Installation 📦

1. Clone the repository:
```bash
git clone https://github.com/Bishusus/Mini-Search-Engine.git
cd Mini-Search-Engine
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

3. No external dependencies required! The project uses only Python standard library modules.

## Usage 🚀

### Basic Usage

1. **Prepare your text files**: Place all `.txt` files you want to search in the `textFiles` directory.

2. **Run the search engine**:
```bash
python main.py
```

3. **Enter your search query** when prompted:
```
Enter your search query: machine learning
```

4. **View results**: The engine will display the top 10 most relevant documents ranked by relevance score:
```
Top 10 relevant documents:
Rank 1. document1.txt: 4.5231
Rank 2. document2.txt: 3.8912
Rank 3. document3.txt: 2.1456
...
```

### Example

Create a simple text file `sample.txt` in the `textFiles` directory:
```
Artificial Intelligence and Machine Learning are revolutionizing technology.
Machine Learning models require large amounts of data for training.
Deep Learning is a subset of Machine Learning focused on neural networks.
```

Then run the search engine and search for "machine learning":
```bash
python main.py
Enter your search query: machine learning
```

## How It Works 🔧

### Algorithm Overview

1. **Document Loading**: All `.txt` files from the `textFiles` directory are loaded into memory.

2. **Tokenization**: Documents are converted into tokens (words), with common stopwords removed.

3. **Inverted Index Creation**: An index is built that maps each token to the documents containing it and frequency counts.

4. **Query Processing**: User queries go through the same tokenization process.

5. **TF-IDF Scoring**: For each document, the engine calculates:
   - **TF (Term Frequency)**: `1 + log(count of term in document)`
   - **IDF (Inverse Document Frequency)**: `log((total documents + 1) / (documents containing term + 1)) + 1`
   - **Score**: `TF × IDF` summed across all query terms

6. **Ranking**: Documents are ranked by their TF-IDF scores in descending order, with top 10 displayed.

## Example Output

```
Enter your search query: python programming

Top 10 relevant documents:
Rank 1. python_tutorial.txt: 8.4532
Rank 2. programming_basics.txt: 5.2341
Rank 3. web_development.txt: 3.1245
```

## Performance Considerations ⚡

- **Indexing Time**: O(n × m) where n is number of documents and m is average document size
- **Search Time**: O(q + k log k) where q is number of query terms and k is number of matching documents
- **Memory Usage**: Proportional to total vocabulary size and document count

## Future Enhancements 🔮

- [ ] Phrase queries support
- [ ] Boolean operators (AND, OR, NOT)
- [ ] Fuzzy matching for typo tolerance
- [ ] Weighted document categories
- [ ] Cache for frequently searched terms
- [ ] Multi-threaded indexing for large document sets
- [ ] Support for PDF and other file formats
- [ ] Web interface/REST API

## Project Structure

This project demonstrates core Information Retrieval concepts:
- **Inverted Index**: Efficient data structure for full-text search
- **TF-IDF**: Standard metric for document relevance scoring
- **Tokenization**: Text preprocessing and normalization
- **Stopword Removal**: Improving search quality by filtering noise

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## File Structure

- **main.py**: Application entry point
- **search_engine/__init__.py**: Package initialization
- **search_engine/loader.py**: Document loader
- **search_engine/tokenizer.py**: Text tokenizer
- **search_engine/indexer.py**: Index builder
- **search_engine/search.py**: Search implementation
- **textFiles/**: Directory for text documents

## License

This project is open source and available for educational and personal use.

## Author

**Bishusus** - Created as a demonstration of search engine implementation principles

## Support & Contribution

Feel free to fork this project, submit issues, or create pull requests with improvements and enhancements!

---

**Happy Searching!** 🎯
