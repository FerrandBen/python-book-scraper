import requests
from requests.exceptions import HTTPError, Timeout, RequestException


def fetch_page(url):

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.text
        return data
    except Timeout:
        print("La requête a dépassé le délai (timeout).")
        return None
    except HTTPError as e:
        print(f"Erreur HTTP: {e.response.status_code}")
        return None
    except RequestException as e:
        print(f"Erreur réseau: {e}")
        return None
