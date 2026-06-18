"""
Lambda Expression (Lambda Funktion)
anonyme Funktion, erzeugt immer ein Funktionsobjekt

lambda parameter1, parameter2: paramater1 + parameter2
"""

fn0 = lambda a, b: a + b


def fn1(a, b):
    return a + b


print(type(fn0), type(fn1))
fn0(1, 2)
fn1(1, 2)
