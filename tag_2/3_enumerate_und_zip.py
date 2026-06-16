"""
enumerate: Loop-Durchgänge nummerieren
zip (Reißverschluss): zwei oder mehrere Iterables
"""
students = ["Bob", "Alice", "Mallory", "Grumpy"]
grades = [1, 2, 3, 1]

for index, student in enumerate(students):
    print(index, student, grades[index])

# print(list(enumerate(students)))
print("*" * 40)
cities = ["Hamburg", "Nürnberg", "Berlin", "Tokyo"]
students = ["Bob", "Alice", "Mallory", "Grumpy"]
grades = [1, 2, 3, 1]

if len(cities) == len(students) == len(grades):
    for name, grade, city in zip(students, grades, cities):
        print(name, grade, city)