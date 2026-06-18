"""
CSV Dateien lesen und schreiben
"""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent


def read_csv(filename: str) -> list:
    """CSV Datei in Liste lesen."""
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        result = []
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)

    return result


def json_data(filename: str, data: list) -> None:
    """Liste von Dicts in Json schreiben."""
    file = DATA_DIR / (filename + ".json")
    with open(file, encoding="utf-8", mode="w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# wie muss man das nach Json schreiben?
result = read_csv("data.csv")
json_data("dataout", result)
print(result)
