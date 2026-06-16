"""
- break (loop abbrechen), 
- continue (aktuelle Iteration abbrechen)
"""
servers = ["serv3.prod", "serv2.DEV", "www.home"]

# break beendet die aktulle Schleife
for server in servers:
    print("Current Server:", server)
    if "serv2.dev" in server.lower():
        print("ja, serv2.dev ist vorhanden.")
        break

# Continue: aktuellen Durchlauf abbrechen
for server in servers:
    if "serv" in server.lower():
        print("Serv-Server brauchen kein Backup")
        continue 

    print("Mache Backup:", server)