"""
Funktionen: haben Parameter, Docstring und Rückgabewert

generell gilt: Funktionen sollen nur eine Aufgabe haben.
"""

MAX_LENGHT = 42  # Konstante, rein technisch gesehen eine Variable

from typing import Any


def filter_urls(urls: list[str], folder: str) -> list[str]:
    """Filtere URLs nach Domain.

    Das hier ist der Beschreibungtext,
    der auch mehrzeilig sein kann und
    bei komplexen Funktionen verwendet wird.

    Args:
        urls: Liste von Urls
        folder: der Folder, wo die DAteien liegen

    Returns:
        eine gefiltere Liste von urls
    """
    threshold = 3
    MAX_LENGHT = 1  # shadowing

    print("MAX LENGHT aus global:", MAX_LENGHT)
    print("Lokale Variablen von filtered_urls:", locals())
    if MAX_LENGHT > 5:
        return []

    return urls


urls = ["domain.xyz", "server.prod"]
filtered_urls = filter_urls(urls, "docs")
print("Urls aus global:", urls)
# print("Globale Variablen:", globals())
