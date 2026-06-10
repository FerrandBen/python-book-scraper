import dataclasses
import json
import csv

JFILE_PATH = "data/book.json"
CFILE_PATH = "data/book.csv"


def export_json(books):

    data = [dataclasses.asdict(book) for book in books]

    with open(JFILE_PATH, "w") as file:
        json.dump(data, file)


def export_csv(books):

    with open(CFILE_PATH, "w", newline="") as csvfile:
        fieldnames = ["title", "price", "score", "availability"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([dataclasses.asdict(book) for book in books])
