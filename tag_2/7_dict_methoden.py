"""
Dict Methode: 
keys() => liefert uns alle Keys eines Dicts
values() => liefert eine Liste aller Values
items() => liefert Tuple von Key-Value-Paaren
"""

person = {
    "name": "Bob",
    "age": 43,
    "hobbies": ["Tennis", "Coding"]
}
print(person.keys())  # dict_keys(['name', 'age', 'hobbies'])
print(person.values()) # ['Bob', 43, ['Tennis', 'Coding']]
print(person.items())

# NOrmale Iteration gibt nur die Keys aus
for entry in person:
    print("=>", entry)

# Iteration über Key-Value Paare
for key, value in person.items():
    print(key, value)
    # Aufgabe: prüfen, ob value eine liste ist (zb. isinstance)
    # wenn ja, dann über die Liste iterieren
    if isinstance(value, list):
        for entry in value:
            print(entry)

"""
# Aufgabe: Gebe jeweils den Vornamen aus
namen = {
    "lists": [
        {"name": "Peter"},
        {"name": "Daniel"},
        {"name": "Abdelrahman"},
    ]
}
"""
namen = {
    "lists": [
        {"name": "Peter"},
        {"name": "Daniel"},
        {"name": "Abdelrahman"},
    ]
}
print(type(namen["lists"][0]["name"]))