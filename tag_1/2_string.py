""" 
Zeichenkette: unveränderlicher Datentyp
"""
string = "Spam"
string2 = 'Spam'
print(type(string))

# Mehrzeiliger
string3 = """
hallo welt,
das ist toll
supertoll
"""
print(string3)

# Anführungszeichen
"Bob sagte 'es war toll'"
"Bob sagte \"es war toll\""

# Strings verbinden
a = "AA"
b = "BB"
c = a + "1" + b # String konkatenieren
print("C:", c)

# Ein String ist eine Sequenz (Reihenfolge)
username = "Alice"
print("Erste Zeichen von einem String:", username[0])
print("Letzte Zeichen von einem String:", username[-1])
print(username[5])