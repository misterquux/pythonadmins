"""
Das import Statement
"""

import pathlib
import sys
from random_lib import get_random_number
import random as randy


# print(
#     type(random_lib),
# )

BASE_DIR = pathlib.Path(__file__)

print("Alles was hier liegt, wird gefunden:", sys.path)
print(
    "Alles, was schon geladen wurde:",
)
for name, path in sys.modules.items():
    # print(name, path)
    pass
