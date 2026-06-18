"""
Schreibe eine Funktion zum Anlegen eines Benutzerkontos
(create_user), die einen Benutzernamen und eine E-Mail-Adresse
 benötigt sowie die optionalen Einstellungen Rolle und Aktiv-Status
 besitzt. Rufe die Funktion anschließend mehrfach auf und verwende
 dabei sowohl Positionsargumente als auch benannte
 (Keyword-)Argumente, um die optionalen Werte gezielt zu ändern.
"""


def create_user(username, email, role="user", active=True):
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Role: {role}")
    print(f"Active: {active}")
    print()


# Nur Positionsargumente
create_user("max", "max@example.com")

# Keyword-Argumente in anderer Reihenfolge
create_user(email="anna@example.com", username="anna")

# Optionale Rolle ändern
create_user("admin1", "admin@example.com", role="admin")

# Optionale Aktivierung ändern
create_user("tom", "tom@example.com", active=False)

# Alle Argumente als Keywords
create_user(
    username="sarah",
    email="sarah@example.com",
    role="moderator",
    active=True,
)
