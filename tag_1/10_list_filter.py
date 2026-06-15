""" 
Best practice zum Filtern von Listen

# Ziel: auf Basis dieser Liste
[23, 2, 8, 42]

eine neue Liste erstellen, die nur Elemente enhält, die > 8 sind
"""
values = [23, 2, 8, 42]
filtered_values = []

# über jedes Element in values iterieren
for value in values:
    if value > 8:
        filtered_values.append(value)

print(filtered_values)


