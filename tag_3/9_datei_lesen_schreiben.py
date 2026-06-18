"""
Dateien einlesen und schreiben
"""

from pathlib import Path


DATA_DIR = Path(__file__).parent


def read_file(filename: str) -> None:
    """Lese Datei ein und gebe den Inhalt aus."""
    f = open(DATA_DIR / filename, encoding="utf-8")
    content = f.read()  # liest ganze Datei in STring content
    print(content)
    print(int(content))
    f.close()


def read_file_better(filename: str) -> None:
    """Lese Datei ein und gebe den Inhalt aus."""

    # with open öffnent einen Kontext-Manager, der garantiert,
    # das das Filehandle wieder geschlossen wird
    # nachdem über f iteriert wurde, ist der filehandler "verbraucht"
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        for line in f:
            print(line.strip())


read_file_better("data.txt")

# Aufgabe: lese sys.log ein und speichere nur die Zeilen, die OK sind
# die Zahlen sollen als float konvertiert werden
# [ ["S1",20.0,"OK"],
#   ["S4",21.5,"OK"]
# ]
result = []

with open(DATA_DIR / "sys.log", "r") as f:
    for line in f:
        parts = line.strip().split()

        if parts[-1] == "OK":
            entry = [
                parts[0],  # z.B. "S1"
                float(parts[1]),  # z.B. 20.0
                parts[2],  # "OK"
            ]
            result.append(entry)

print(result)


# Datentyp set

x = ["ameri", "ameri", "a"]
print(list(set(x)))
