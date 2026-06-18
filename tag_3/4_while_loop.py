"""
Der While-Loop
"""

print("Press 1 to launch rocket, exit or quit to quit")

while True:
    ui = input("Was willst du tun?").lower()
    if ui in ["quit", "exit", "goodbye"]:
        break
    if ui == "1":
        print("launching rocket...")

print("Programm beendet")
