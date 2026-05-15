from src.search import find_query

def test_find_query(capsys):

    index = {
        "indifference": {
            "page1": {}
        },
        "good": {
            "page2": {}
        },
        "friends": {
            "page2": {}
        },
    }

    find_query(index, "good friends")
    captured = capsys.readouterr()

    assert "page2" in captured.out