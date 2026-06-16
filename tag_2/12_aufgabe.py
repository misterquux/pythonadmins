"""
Aufgabe. Schreibe eine funktion `add_life_points`
die einen Spielernamen und Lebenspunkte übergeben bekommt.

add_life_points("gollum", 10)

Die Funktion soll dem globalen player_stat für den
übergebenen Spieler die Lebenspunkte hinzufügen.

Hier findet ein sogenannter `Seiteneffekt` statt.
Seiteneffekte will man in der Regel vermeiden, aber manchmal -wie hier-
sind sie nützlich.
"""

player_stat = {
    "bilbo": {
        "life": 100,
        "power": 29,
        "weapons": {"knife", "stick"},
    },
    "gollum": {
        "life": 120,  # +10
        "power": 29,
        "weapons": set(),
    },
}


def add_life_points(playername, lifepoints):
    # player_stat[playername]["life"] = player_stat[playername]["life"] + lifepoints
    player_stat[playername]["life"] += lifepoints


add_life_points("gollum", 10)
print(player_stat)
