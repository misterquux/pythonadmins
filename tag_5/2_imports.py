"""
Beispiel, wie ich Module aus einem Paket importieren kann

import my_package => geht in der Regel nicht, da man keine Pakete importieren kann
"""

# from my_package import beta, alfa  : BEST PRACTICE
# beta.b()
import sys

# TIP: Modulsuchpfad ausgeben bei Modulenotfound-error
print("MODUL SUCHPFAD:", sys.path)

import my_package.beta as beta
# print(my_package.beta.b())

beta.b()
