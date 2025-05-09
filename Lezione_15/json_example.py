import json

PATH = "Lezione_15/config.json"
mode: str = "r"
encoding: str = "utf-8"

config = None

with open(PATH, mode=mode, encoding=encoding) as file:
    config: dict = json.load(file)

# Corretto: uso di apici singoli all'interno
# print(f"Host: {config['server']['host']} Port: {config['server']['port']}")

# Modifiche al dizionario
config["AGGIUNTA"] = "NUOVO"
config["server"]["host"] = "google.it"

# Salvataggio nel file
with open(PATH, mode="w", encoding=encoding) as file:
    json.dump(config, file, indent=4)


