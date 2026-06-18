"""
Eine externe JSON-Api konsumieren und in eine Datei schreiben.
requests, pip install requests

- so wenig globale Variablen wie möglich

https://jsonplaceholder.typicode.com/todos


Python                  JSON
-----------------------------------------
dict                =>  object
list, tuple         =>  array
str                 =>  string
int, float          =>  number
True                =>  true
False               =>  false
None                =>  null

STRG + SHIFT + P => Vs Code Controllcenter
"""

import json
from pathlib import Path

import requests

URL = "https://jsonplaceholder.typicode.com/todoss"


def load_json(url: str):
    """Lade JSON von einem entfernten Server."""
    response = requests.get(url)
    response.raise_for_status()  # Exception auslösen, wenn Status-Status
    return response.json()


def process_data(data: list, user_id: int) -> list:
    """Filtere Daten nach User ID."""
    filtered_data = []
    for todo in data:
        if user_id == todo["userId"]:
            filtered_data.append(todo)
    return filtered_data


def save_data(data: list) -> None:
    """Schreibe Json in eine Datei."""
    # Datei im Schreibmodus öffnen
    file = Path(__file__).parent / "data.json"
    # Datei `file` anlegen im Modus w
    with open(file, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_data(filename: Path) -> list:
    """Aufgabe: Implementiere die Funktion und nutze zum
    Einlesen der json.load(f). mode='r'"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)


def main():
    try:
        data = load_json(url=URL)
    except requests.exceptions.HTTPError as e:
        print(f"Es wurde ein HTTP Fehler ausgelöst: {e}")
        return
    except Exception as e:
        print(f"Es ist ein unbekannter Fehler aufgetreten: {e}")
        return

    filtered_data = process_data(data, user_id=1)
    save_data(filtered_data)

    file = Path(__file__).parent / "data.json"
    data = load_data(filename=file)
    print("*" * 40)
    print(data)


main()
