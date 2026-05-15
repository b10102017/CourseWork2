from src.indexer import tokenize
import json

def print_word(index, word):

    word = word.lower()

    if word in index:

        print(json.dumps(index[word], indent=4))

    else:
        print("Word not found.")


def find_query(index, query):

    words = tokenize(query)

    if not words:
        print("Empty query.")
        return

    page_sets = []

    for word in words:

        if word in index:

            pages = set(index[word].keys())
            page_sets.append(pages)

        else:
            print("No results found.")
            return

    results = set.intersection(*page_sets)

    if results:

        print("\nMatching pages:")

        for page in results:
            print(page)

    else:
        print("No matching pages found.")