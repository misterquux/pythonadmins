"""
Funktionsparameter
"""


def summe(a, b):
    """Funktion summe hat zwei Parameter"""
    print(f"{a=}, {b=}")  # f"a={a}"


summe(1, 2)  # Positionelle Argumente, es werden zwei Argumente benötigt


#############################################################
# positionelle Argumente
#############################################################
def save_database(host, port, force_delete=False):
    """Funktion hat 3 Parameter, force_delete hat einen
    Defaultwert"""
    print(f"{host=}, {port=}, {force_delete=}")


save_database("localhost", 1723)
save_database("localhost", 1723, True)  # True überschreibt False


#############################################################
# Keyword Argumente (benannte Argumente)
#############################################################
def set_encoding(filename, encoding, offset=0, byteorder="le"):
    print(f"{filename=}, {encoding=}")


# normaler Aufruf
set_encoding("blabubb.txt", "uft-8", 1, "le")
set_encoding(encoding="utf-8", filename="servers.csv", byteorder="be")


# Das Sternchen bedeuet: alles rechts davon muss per Keyword
# Argument übergeben werden.
def connect_to_db(username: str, *, password: str, database: str) -> int:
    pass


connect_to_db("otto", database="local", password="abc123")
# connect_to_db("otto", "local", "abc123")
