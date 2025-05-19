def esercizio6():

    menu:dict = {"Pizza": 9.00, "Pasta": 10.50, "Zuppa" : 7.00,
    "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20,
    "Patatine Fritte": 5.50, "Patate al forno": 5.50, "Verdura del giorno": 7.00,
    "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia con Nutella": 6.00,
    "Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.00}

    ordine:dict = {}

    ordine["Pizza"] = menu["Pizza"]
    ordine["Salmone"] = menu["Salmone"]
    ordine["Tiramisu"] = menu["Tiramisu"]
    ordine["Vino"] = menu["Vino"]

    print(ordine)
    
    sum:int = 0
    for value in ordine.values():
        sum += value
    
    print(sum)


esercizio6()



