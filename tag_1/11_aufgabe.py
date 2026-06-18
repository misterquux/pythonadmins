"""
Lege eine Liste mit den Namen von fünf Servern an.
FIltere anschließend alle Servernamen, die "web" enthalten,
und speichere in einer neuen Liste

web01
web02
db01
mail01
backup01

printe die Ergebnisliste in einem Loop
"""

servers = [
    "web01",
    "web02",
    "db01",
    "mail01",
    "backup01",
]

web_servers = [server for server in servers if "web" in server]

for server in web_servers:
    print(server)
