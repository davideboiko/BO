opzione:list[str] = ["ingresso", "uscita", "stato", "esci"]

posti:int = 50
posti_occupati:int = 0
domanda:str = input("Richiesta: ")

while domanda != opzione[3]:
    if domanda == opzione[2]:
        print(posti)
        print(posti_occupati)
    elif domanda == opzione[1]:
        if posti < 50:
            posti += 1
            posti_occupati -= 1
    elif domanda == opzione[0]:
        if posti > 0:
            posti -= 1
            posti_occupati += 1
    else:
        domanda:str = input("Richiesta: ")

