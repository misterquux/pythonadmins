"""
Listen, Teil 2
"""
fruits = ["apple", "cherry"]
print(f"Datentyp von fruits: {type(fruits)}") # Objekte

if isinstance(fruits, list):
    print("Objetk fruits ist eine Liste")

values = [1, 2, 3, "423"]
calculated_list = []
for value in values:
    if isinstance(value, (int, float)):
        value = value + 0.1
        calculated_list.append(value)
    else:
        if value.replace(".", "").isdigit():
            value_numeric = float(value)
            calculated_list.append(value_numeric)

print(calculated_list)
print(dir(calculated_list))