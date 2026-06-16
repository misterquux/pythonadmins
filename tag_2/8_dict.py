"""
Zwei Dicts verbinden
"""
config = {
    "sys": 42,
    "path": "/tmp/schrott"
}

custom_config = {
    "command": "ls -al",
    "path": "/tmp/custom"
}

# {'sys': 42, 'path': '/tmp/schrott', 'command': 'ls -al'}
gesamt_config = config | custom_config
print("mit Pipe:", gesamt_config)

# vor python 3.9 muss das so gemacht werden
gesamt_config = {**config, **custom_config}
print("**-Schreibweise:", gesamt_config)

# Config Dict updaten mit neuen Key - Value Paaren
config.update(custom_config)
print("Config nach UPdate:", config)