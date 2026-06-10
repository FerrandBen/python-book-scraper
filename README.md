# 📝 Python Book Scraper

Un scraper de livres en Python

---

## ✨ Fonctionnalités

- Requêtage du site https://books.toscrape.com/
- Récuperation des livres
- Persistance des données en JSON et en CSV
- Gestion des erreurs et validation des entrées

---

## 🛠️ Stack technique

- Python 3.13
- `dataclasses` — modélisation des données
- `json` — persistance des données
- `csv` — persistance des données
- `requests` — Requêtage HTTP
- `beautifulsoup4` — parsing HTML

---

```
python-book-scraper/
│
├── scraper/
│   ├── __init__.py
│   ├── book.py         # Modèle de données Book
│   ├── exporter.py     # Persistance JSON et CSV
│   ├── fetcher.py      # Requêtage de l'URL (GET)
│   └── parser.py       # Récuperation des informations
│
├── data/
│   ├── book.csv        # Données sauvegardées
│   └── book.json       # Données sauvegardées
│
├── main.py             # Point de lancement du programme
└── README.md
```

---

## 💡 Concepts pratiqués

- Requêtes HTTP avec requests
- Parsing HTML avec Beautifulsoup4
- Modélisation des données avec dataclasses
- Export de données en JSON et CSV

---

## ⚙️ Installation

- git clone https://github.com/FerrandBen/python-book-scraper
- Créer et activer le venv
- pip install -r requirements.txt

---

## 🚀 Utilisation

- Lancement du programme via la commande : python main.py