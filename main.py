from scraper.fetcher import fetch_page
from scraper.parser import parse_books
from scraper.exporter import export_json, export_csv

URL = "https://books.toscrape.com/"
if __name__ == "__main__":

    html = fetch_page(URL)

    if html is None:
        print("Erreur HTML manquant")
    else:
        book_list = parse_books(html)
        export_json(book_list)
        export_csv(book_list)
        print(f"{len(book_list)} livres exportés avec succès !")
