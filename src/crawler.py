# import necessary libraries
import requests
from bs4 import BeautifulSoup
import time

URL = "https://quotes.toscrape.com"

# function to crawl the website and extract text content from each page
def crawl_site():
    """
    Returns:
    dict {url: text_content}
    """
    # Dictionary to store the content of each page with URL as key and text content as value
    pages_content = {}

    url = URL

    # Loop to crawl through all pages until there are no more pages to crawl
    while url:

        print(f"Crawling: {url}")

        response = requests.get(url)

        # Check if the request was successful. If not, print an error message and break the loop
        if response.status_code != 200:
            print("Failed to retrieve page.")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")

        page_text = ""

        for quote in quotes:
            page_text += quote.get_text() + " "

        pages_content[url] = page_text

        # Find the link to the next page. If there is no next page, set url to None to exit the loop
        next_button = soup.find("li", class_="next")

        if next_button:
            next_link = next_button.find("a")["href"]
            url = URL + next_link
        else:
            url = None

        # Politeness window
        time.sleep(6)

    return pages_content