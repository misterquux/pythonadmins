"""
Arbeiten mit Pfaden
"""

from pathlib import Path

# aktuelle Arbeitsverzeichnis
print("CWD:", Path.cwd())

path_to_kurs = r"C:\Users\Administrator\python_kurs"
path_to_kurs: Path = Path(path_to_kurs)

print("Parentpath:", path_to_kurs.parent)

neuerpfad = path_to_kurs.parent / "data" / "files"
# exist_ok=True
neuerpfad.mkdir(parents=True, exist_ok=True)

# Absoluter Pfad zu dem Python-Script
print(__file__)
current_directory = Path(__file__).parent
print("Verzeichnis des Scripts:", current_directory)


# Rekursive Suche nach allen Python-Dateien
# for path in base_dir.glob("*.py"):
for path in current_directory.rglob("*.py"):
    print(path)
