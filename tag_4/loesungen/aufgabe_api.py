from collections import Counter
import logging
import random
import time

import requests

API_URL = "https://naas.isalman.dev/no"

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def fetch_reason() -> str:
    """Holt den reason-Text von der API."""
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["reason"]


def run_requests(n: int) -> tuple:
    """
    Führt n API-Requests aus und zählt Duplikate mit Counter.
    """
    results: dict[int, str] = {}
    counter: Counter = Counter()

    success = 0

    for i in range(n):
        try:
            reason = fetch_reason()
            results[i] = reason
            counter[reason] += 1
            success += 1
            logger.info("SUCCESS")

        except Exception as e:
            results[i] = "ERROR"
            logger.error(e)

        time.sleep(random.uniform(0.1, 0.6))

    return results, counter


def main() -> None:
    n = int(input("Anzahl Requests: ").strip())
    results, counter = run_requests(n)

    print("\n=== Ergebnis ===")
    print("Requests:", n)
    print("Erfolgreich:", sum(1 for v in results.values() if v != "ERROR"))
    print("Fehler:", sum(1 for v in results.values() if v == "ERROR"))

    print("\n=== Duplikate (>1) ===")
    for text, count in counter.items():
        if count > 1:
            print(f"{text} -> {count}x")


if __name__ == "__main__":
    main()
