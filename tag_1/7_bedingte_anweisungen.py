""" 
Bedingte Anweisungen (if - else - elif)

>, >=
<, <=
==  => gleich
!=  => ungleich
in-Operator (Identitäts-Operator)

"""
a = 3 
b = 2

if a > b:
    print("a ist größer als b")

csv_string = "aa,aa"  # Sequenzen
if "," in csv_string:
    print("der CSV-String beinhaltet ein Komma.")


el = "03LiNux05"
if "linux" in el.lower():
    print("linux ist enthalten")


############ Strings vergleichen (equals) ==
a = "hamburg"
b = "hamburg"

if a == b:
    print("Strings sind gleich")
else:
    print("Strings sind ungleich")

a = 3
b = 4
if a > 3:
    print("a > 3")
elif b < 5:
    print("b < 5")


# ODER
if (a == b) or ("burg" in "Nürnberg"):
    pass

# NOT
if "a" not in "Berlin":
    print("a ist nicht in Berlin")

# UND
severity = "high"
if "prod" in "prod.server2" and severity == "high":
    print("Alarm")


# logische Operatoren: and, or, not (&&, |, !)

# Truthyness: alles wahr, was nicht: 0, "", [], {}

ergebnis = 0
if ergebnis:
    print("Ergenbis ist ungleich 0")
else:
    print("Ergebnis ist 0")


city = ""
if city:
    print(f"City ist {city}")
else:
    print("City ist leer")