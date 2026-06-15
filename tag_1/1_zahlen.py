"""
Zahlen (3 Datentyp)
- Ganzzahlen (Integer)
- Fließkommazahlen (Float, 64bit)
- Komplexe Zahlen

Arithmetische Operatoren

x + y   Summe von x und y
x - y   Differenz von x und y
x * y   Produkt von x und y
x / y   Quotient von x und y
x % y   Rest beim Teilen von x durch y*
+x  positives Vorzeichen
-x  negatives Vorzeichen
x ** y  x hoch y
x // y  abgerundeter Quotient von x und y*

"""
x = 3 # ein Integer (bzw. ein Integer-Objekt)
print("Typ von x:", type(x)) # <class 'int'>

y = 42.2 # Float
print("Typ von y:", type(y)) # <class 'float'>

# x / y   Quotient von x und y
x = 4
y = 2
result = x / y  # 2.0
int_neu = int(result) # konvertiere aus result in Int
print("result = x / y:", result, int_neu)


"""
Aufgabe:
Ein Raum fasst maximal 10 Personen. Zur Zeit befinden sich eine
unbekannte Anzahl an Personen in diesem Raum.
Wieviele Personen können den Raum noch betreten?
Lege passende Variablen/Konstanten an und führe die Berechnung durch.

Singular und Plural sowie negative Anzahl an Personen im Ergebnis-Print
sind zu ignorieren.
"""
MAX_PERSONS = 10
#current_persons = int(input("Bitte gebe eine Zahl ein:"))
current_persons = 4
persons = MAX_PERSONS - current_persons
print("Es passen noch", persons, "in den Raum")

