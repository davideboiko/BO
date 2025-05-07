def filtra_e_mappa(prodotti: dict[str, float]) -> dict[str, float]:
    diz: dict[str, float] = {}

    for key,value in prodotti.items():
        if value >= 50:
            value = value * 0.9
        diz[key] = value
    return diz

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Tavolo': 120.0, 'Sedia': 85.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))
print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))
print(filtra_e_mappa({}))