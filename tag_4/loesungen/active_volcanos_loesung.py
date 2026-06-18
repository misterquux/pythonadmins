import csv
import json
from pathlib import Path
from typing import Any

FILE_IN = Path(__file__).parent / "active_volcanos.csv"
FILE_OUT = Path(__file__).parent / "datas/volcanos_germany.json"
COUNTRY = "Germany"


def read_volcanos_by_country(filename: Path, country: str) -> list[dict[str, Any]]:
    volcanos = []

    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Country"] == country and row["risk"] != "NULL":
                volcanos.append(
                    {
                        "name": row["V_Name"],
                        "risk": row["risk"],
                        "lat": row["Latitude"],
                        "long": row["Longitude"],
                        "country": row["Country"],
                        "region": row["Region"],
                    }
                )

    return volcanos


def write_json(filename: Path, data: list[dict[str, Any]]) -> None:
    FILE_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main() -> None:
    volcanos = read_volcanos_by_country(FILE_IN, COUNTRY)
    write_json(FILE_OUT, volcanos)
    print(volcanos)


if __name__ == "__main__":
    main()
