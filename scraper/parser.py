from bs4 import BeautifulSoup
from .fetcher import fetch_page
from .book import Book

SCORES = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_books(html):

    books = []

    soup = BeautifulSoup(html, "html.parser")

    articles = soup.find_all("article", class_="product_pod")

    for item in articles:
        books.append(parse_book(item))
    return books


def parse_book(article):

    title = article.find("h3").find("a")["title"]
    price = float(article.find("p", class_="price_color").get_text().replace("£", ""))
    score = SCORES[article.find("p", class_="star-rating")["class"][1]]
    availability = bool(article.find("p", class_="instock availability"))

    return Book(title=title, price=price, score=score, availability=availability)
