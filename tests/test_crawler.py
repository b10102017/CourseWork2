from src.crawler import crawl_site

def test_crawl_site():

    pages = crawl_site()

    assert len(pages) > 0

    for url, text in pages.items():

        assert "https://quotes.toscrape.com" in url
        assert len(text) > 0