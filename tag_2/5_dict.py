"""
Datentyp dict (eine Hashmap Implementierung in Python)
Key-Value Speicher
"""
d = {}  # Dictory Literal
d = {"a": 3, "b": [3, 1]}  # Key eines Dicts muss unveränderlich
print("Dictionary d:", d)

en_de = {
    "cat": "katze",
    "dog": "Hund"
}
print("Katze auf deutsch:", en_de["cat"])  #animals[3]

# mit in Operator prüfen, ob der Key "dog" enthalten ist
if "dog" in en_de:
    en_de["dog"]
else:
    print("key dog ist nicht enthalten")
    en_de["dog"] = "Hund"

# Dict ist veränderbar
en_de["mouse"] = "Maus"

# GET - Methode (produziert keinen Fehler, wenn key nicht enthalten ist)
print(en_de.get("bird", "generisches Tier"))

print(bool(en_de.get("bird")))  # False
print(bool(en_de.get("mouse")))  # False