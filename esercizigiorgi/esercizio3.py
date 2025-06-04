def macheneso():
    prodotti:dict = {"pasta": 45, "pizza": 46,
                      "lasagna": 49, "bo": 50,
                        "bo1": 51, "bo2": 52} 
    prodprez = {}
    for key, value in prodotti.items():
        if value < 50:
            prodprez[key] = round(value + (value * 0.1))

    return prodprez

print(macheneso())

