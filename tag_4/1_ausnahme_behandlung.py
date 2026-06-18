"""
Exception Handling: Ausnahmebehandlung (Alternative: loguru)

DEBUG
INFO
WARNING
ERROR
CRITICAL

siehe auch: https://python-admins.friendlybytes.net/chapter_10/
"""

import logging

# einen Logger bauen, der alles loggt ab level DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# jeder Logger benötigt mindestens einen Handler, der die
# Log-Message verarbeitet. Hier nutzen wir einen Streamhandler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# das ist das Format der Log-Messages, die wir dem
# Handler zuwsisen
a_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
stream_handler.setFormatter(a_format)

# Am Ende muss man dem logger noch die Handler zuweisen.
# hier weisen wir dem logger unseren STream-Handler zu
logger.addHandler(stream_handler)

# so loggen wir
logger.info("Eine Info Message")

user_eingabe = "0.2a"
try:
    value = float(user_eingabe)
    print(f"Floatwert: {value}")
except ValueError as e:
    print(f"Es ist ein Fehler: {e}")
except Exception as e:
    print(f"es ist ein Fehler aufgetreten: {e}, {type(e)}")
