# import necessary libraries
import json
import re
from collections import defaultdict

INDEX_FILE = "data/index.json"

def tokenize(text):
    """
    Convert text to lowercase and split into words.
    """

    return re.findall(r"\w+", text.lower())


def build_index(pages_content):
    """
    Build inverted index.
    """

    inverted_index = defaultdict(dict)

    for url, text in pages_content.items():

        words = tokenize(text)

        for position, word in enumerate(words):

            if url not in inverted_index[word]:

                inverted_index[word][url] = {
                    "frequency": 1,
                    "positions": [position]
                }

            else:

                inverted_index[word][url]["frequency"] += 1
                inverted_index[word][url]["positions"].append(position)

    return dict(inverted_index)


def save_index(index):

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=4)

    print("Index saved.")


def load_index():

    with open(INDEX_FILE, "r") as f:
        index = json.load(f)

    print("Index loaded.")

    return index