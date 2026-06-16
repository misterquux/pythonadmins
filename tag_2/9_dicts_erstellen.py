""" 
Dicts aus zwei listen erstellen
"""
countries = ["Argentinien", "Türkei", "USA", "Russland", "Spanien"]
food = ["Alfajores", "Pilav", "Hamburger", "Pelmeni", "Empanada"]

d = dict(zip(countries, food))
print(d)


# Dict aus einer Liste von Listen
alphabet = [
    ["A", "aleph"],
    ["B", "beth"]
]
d = dict(alphabet)

# Word-Counter (for, split, dict, )
# Sentence splitten. über Ergebnisliste iterierne
# prüfen, ob Wort in dict: wenn ja, increment, wenn nein: einfügen ins dict
sentence = "the quick brown fox jumps over the fox"
# Ausgabe
# {
#     "the": 2,
#     "quick": 1,
#     "fox": 2
# }

d = {
    "b": 1
}

if "a" in d:
    d["a"] = d["a"] + 1
else:
    #? neuen Key mit WErt 1 einfügen?
    d["a"] = 1