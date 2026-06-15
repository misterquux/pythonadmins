"""
Format-String
"""
hours = 3
print("Der User arbeitet seit", hours, "Stunden")
msg = "Der User arbeitet seit" + str(hours) + "Stunden"

hours = 42
room = "AB"
msg = f"Der User arbeitet seit {hours} Stunden in Raum {room}"
print(msg)

input("Bitte gebe deine Körpergröße ein")