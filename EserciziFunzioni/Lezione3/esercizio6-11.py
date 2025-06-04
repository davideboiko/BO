citta = {
    "Roma": {
        "paese": "Italia",
        "popolazione": "2.8 milioni",
        "fatto": "È famosa per il Colosseo e l'antica civiltà romana."
    },
    "Tokyo": {
        "paese": "Giappone",
        "popolazione": "14 milioni",
        "fatto": "È la città più popolosa del mondo."
    },
    "New York": {
        "paese": "Stati Uniti",
        "popolazione": "8.5 milioni",
        "fatto": "È chiamata 'La Grande Mela'."
    }
}

# Stampa tutte le informazioni
for nome_citta, info in citta.items():
    print(f"\nCittà: {nome_citta}")
    print(f"  Paese: {info['paese']}")
    print(f"  Popolazione: {info['popolazione']}")
    print(f"  Fatto interessante: {info['fatto']}")
