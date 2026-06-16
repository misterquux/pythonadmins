"""
Datentyp Tuple: unveränderlicher Daten
"""
# Liste sollte homogen sein, dh. nur Elemente gleichen Datentyps
names = ["Bob", "Alice"]
names[0] = "Bobby"

print(list(enumerate(names)))


# Tupel anlegen (heterogen erwünscht)
x = 1, 2
y = (1, "2", 3.3)
z = (1,)
print("Tupel z:", type(z)) # <class 'tuple'>

# Person
bob = ("Bob", 23, "Developer")
print(bob[0])

# die drei Elemtene von Bob an Variablen zuweisen
name = bob[0]
age = bob[1]
job = bob[2]

# in Python macht man Unpacking
# Unpacking von Tuples (allgemeiner Sequenzen)
name, age, job = bob #  ("Bob", 23, "Developer")
print("tuple bob:", bob)
print("Tuple bob entpackt:", name, age, job)

name, *args = bob
print("Name:", name) # Bob
print("*args", args) # [23, 'Developer']

# Welcher Datentyp ist value?
for value in enumerate(names):
    index, name = value
    print(index, name)

for index, name in enumerate(names):
    print(index, name)
##################

nullpunkt = (0,0)
# nullpunkt[0] = 1