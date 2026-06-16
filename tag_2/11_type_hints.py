"""
Type Hints: Typ-Hinweise in Funktionen
"""

x: int = 3


def summe(a: int, b: int) -> int:
    return a + b


def print_values(values: list[int | float]) -> None:
    print(values)


print(summe(2, 4))
print(summe("2", "4"))  # Typechecker heult weil Zahlen Strings
print_values([1, 2, 3])
print_values([1, 2, 3, 3.2])
