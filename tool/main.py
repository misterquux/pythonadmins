import argparse
from pathlib import Path

import requests

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def download(url: str, force: bool):
    filename = url.replace("://", "")
    target = DATA_DIR / f"{filename}.html"

    if not target.exists():
        print("Lade herunter:", target)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        target.write_text(response.text)

    else:
        print("Datei wurde schon runtergeladen")


if __name__ == "__main__":
    # python main.py --url google.de --force
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        required=True,
        help="Url der Download Datei",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Download erzwingen",
    )
    args = parser.parse_args()
    print("Die Url zum Download:", args.url)
    download(args.url, args.force)
