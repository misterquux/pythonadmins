"""
Sortieren von Listen und Dicts
"""

numbers = [5, 2, 8, 2, 9, 3, 5, 4]
# numbers.sort() => sortiert inplace,
numbers_sorted = sorted(numbers)
print("Numbers sorted:", numbers_sorted)

# Zeichen sortieren (ASCII / Unicode)
chars = ["a", "f", "c", "d", "e"]
chars_sorted = sorted(chars)
print(chars_sorted)

# Groß und kleinschreibung (A=65, a=97)
chars = ["A", "f", "b", "B", "A", "d", "e", "u", "z", "a"]
chars_sorted = sorted(chars, key=lambda el: el.lower())
#
chars_sorted = sorted(chars, key=lambda el: (el.lower(), el.isupper()))
print(chars_sorted)

# Sortiere nach letzter Ziffer
ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
ids_sorted = sorted(ids, key=lambda el: el[-1])
print(ids_sorted)

# Snack nach Price sortieren [(snickers, 1.50), (milka, 3.30), ()]
snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}


# Nach Preis sortieren
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}


from functools import partial


def sortfn(key, el):
    return el[1][key]


# eine Funktion mit einem Argument vorbelegen
snack_nach_preis = sorted(snacks.items(), key=partial(sortfn, "price"))
print(snack_nach_preis)
