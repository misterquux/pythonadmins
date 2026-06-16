"""
Funktionen in Python

Schema:
def function_name(parameter1, parameter2, ...):
    print("ich bin der Funktionskörper")
"""


def hello_world(name):
    print(f"Hello {name}")


hello_world("Alice")  # Argument


def inspect_list(liste):
    """Gebe letztes Element der Liste aus."""
    liste = liste.copy()
    last_element = liste.pop()
    print(last_element)


cities = ["M", "B", "C"]
inspect_list(cities)
print("cities:", cities)
