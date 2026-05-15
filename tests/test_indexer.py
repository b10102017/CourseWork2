from src.indexer import tokenize, build_index

def test_tokenize():

    text = "It cannot be changed without changing our thinking."

    result = tokenize(text)

    assert result == ["it", "cannot", "be", "changed", "without", "changing", "our", "thinking"]


def test_build_index():

    pages = {
        "page1": "indifference",
        "page2": "good friends"
    }

    index = build_index(pages)

    # word exists in index
    assert "good" in index

    # correct page
    assert "page2" in index["good"]

    # frequency count
    assert index["good"]["page2"]["frequency"] == 1