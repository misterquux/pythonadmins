import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

server_list = [
    {"host": "app.03", "port": 443, "location": "Hamburg"},
    {"host": "app.01", "port": 80, "location": "Hamburg"},
    {"host": "app.023", "port": 443, "location": "Nürnberg"},
    {"host": "dev.app.034", "port": 80, "location": "Berlin"},
]


def write_csv(filename: str, data: list[dict]):
    """Serverliste als CSV schreiben."""
    file = DATA_DIR / filename

    with open(file, encoding="utf-8", mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=server_list[0].keys())
        writer.writeheader()  # auf Basis der Fieldnames
        writer.writerows(data)


write_csv("servers.csv", server_list)
