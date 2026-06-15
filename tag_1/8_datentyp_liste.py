"""
Datentyp Liste: eine veränderliche Sequenz
"""
name = ["B", "o", "b"]
name[0] = "P"
print("Neue Liste:", name)

# eine Liste von int und float
values = [12, 42, 15, 23, 23.2]
print("Ertes Element:", values[0])
print("Letztes Element:", values[-1])
print("Vorne und hinten abschneiden:", values[1:-1])

# eine Liste von STrings
cities = ["Berlin", "München", "Nürnberg"]
berlin = cities[0]
print("Berlin:", berlin.upper())


cities_new = cities + ["new york", "chicago"]
backup = cities_new # bei verändlichern Typen wird die Referenz kopiert

cities_new.append("Fürth")
print(cities_new)

# Länge einer Liste (bzw. einer Sequenz)
print("Länge einer Liste:", len(cities_new))

# pop (Das letzte Elemten entfernen)
print(cities_new.pop())
print("Cities nach pop:",cities_new)
print("*" * 50)
print("Backup:", backup)
print("Cities new:", cities_new)