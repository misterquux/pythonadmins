"""
Funktionsobjekt (Python ist alles ein Objekt)
Funktionen sind `First Class Citizens`.
"""


def summe(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = {
    "+": summe,
    "*": multiply,
}

ui = "+"
operations[ui](1, 2)  # summe(1, 2)


def call_function(f):
    f()


def fn():
    """Leere Funktion."""
    print("das hier ist fn")


print(fn)  # Funktionsobjekt, Funktionsreferenz
print(fn.__doc__)
print(fn.__code__.co_firstlineno)
call_function(fn)
