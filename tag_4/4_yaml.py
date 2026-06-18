"""
pyaml
"""

from pprint import pprint
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).parent


def read_config(filename: str) -> None:
    """Yaml Datei einlesen."""
    with open(DATA_DIR / filename, mode="r", encoding="utf-8") as f:
        d = yaml.safe_load(f)
        # pprint(d, width=40)
        return d


def write_config(filename: str, data: dict) -> None:
    """Yaml Datei schreiben."""
    with open(DATA_DIR / filename, mode="w", encoding="utf-8") as f:
        yaml.dump(data, f)


config = read_config("config.yaml")
new_users = [
    dict(name="Grumpy", role="developer"),
    {"name": "Otto", "role": "chef"},
]
pprint(new_users)
print("*" * 40)
config["users"].extend(new_users)
write_config(filename="configneu.yaml", data=config)
