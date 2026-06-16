"""
Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). If the given string already ends 
with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, 
leave it unchanged. Go to the editor

Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
input_string = "abc"
length = len(input_string)

if length > 2:
    if input_string[-3:] == 'ing':
        input_string += 'ly'
    else:
        input_string += 'ing'
print("Input String: ", input_string)



eingabe = input("Bitte gebe ein gültiges Wort ein: ")

if " " in eingabe or eingabe.find("A") < 1 or len(eingabe) < 3:
    print("Ihre Eingabe war: ", eingabe)
    print("Ihre Eingabe ist leider falsch.")
else:
    print("Ihre Eingabe ist korrekt.")

print(eingabe.find("A"))  # 2



servers = ["web01", "web02", "db01", "mail01", "backup01"]
filtered = []

for s in servers:
    if "web" in s:
        filtered.append(s)

for s in filtered:
    print(s)


# Portnummern

ports = [50, 100, 40, 20, 200, 50, 100, 10]
allowed = [50, 100, 200]
result = []

for p in ports:
    if p in allowed:
        result.append(p)

print(result)

# Bereinige Liste
data = ["x_x", "alpha_beta", "_"]
result = []

for el in data:
    el = el.replace("_", "")
    if el:
        result.append(el)

print(result)

# Bereinige Liste
data = ["haxlt ", "\nandx", "\tcatch ", " xfire "]
result = []

for el in data:
    el = el.strip().replace("x", "")
    if el:
        result.append(el)

print(result)

# Server
a = ["server2", "www.prod"]
b = [200, 400]
c = []

i = 0
for server in a:
    c.append(f"{server}: {b[i]}")
    i += 1

print(c)


