"""
das Range Objekt
"""
import time

for i in range(3):
    print(i)

print("*" * 30)

for i in range(2, 9):
    print(i)


servers = ["serv3.prod", "serv2.DEV", "www.home"]
status_code = [400, 200, 403]

for i in range(len(servers)):
    print(f"{servers[i]}, {status_code[i]}")


###############################################
# Wenn der Wert von Range in der Iteration nicht benötigt wird,
# als best practice einen Underscore nutzen: signalisiert, dass 
# der Wert nicht weiter verwendet wird
for _ in range(3):
    print("ping...")
    # time.sleep(0.2)

# Schrittweite
for i in range(0, 4, 2):   # 0, 2
    print(i)

print("*" * 50)
###########################################################
# Aufgabe: people in Gruppen von 3 einteilen und printen
group_size = 3
people = ["a", "b", "c", "d", "e", "f", "g", "h"]
# erwartes ergebnis [a,b,c], [d,e,f], [g,h]
for i in range(0, len(people), group_size):
    print(people[i:i + group_size]) # 0:0+3, 3:3+3