"""
String-Methoden (Funktionen, die auf einem String-Objekt operieren)
jede String-Operation erzeugt neuen String ()
"""
example = "the Quick brown fox jumps"

# replace (ersetze Teile eines Strings mit einem String)
# ERinnerung: jede String-Operation (Methode, Operator) erzeugt neuen
# String
replaced_example = example.replace("o", "XX")
print("Replaced:", replaced_example)

# Mini-Aufgabe: aus folgendem String ein Float erzeugen
wert = "3,14"  # replace, float(wert)
wert = wert.replace(",", ".")  # 3.14
wert = float(wert)

float("a314b".replace("a", "").replace("b", ""))

###############################################
# Startswith und endswith
if example.startswith("th"):
    print("Examplestring fängt mit th an.")

file_name = "a.csv"
if file_name.endswith(".csv"):
    print(file_name)

###############################################
# strip (trim): Whitespace vorne und hinten eines Strings löschen
text = "\n\n der gute Text \t"
print("Text vor Cleaning:", text)
text = text.strip()
print("Text nach Cleaning:", text)

print("*" * 50)


###############################################
# split (einen String aufsplitten)
text = "domain.xyz.csv" # [domain, xyz, csv]
result = text.split(".")  # Leerzeichen ist Default
print(f"Result: {result}", result[0])


# Hamburg