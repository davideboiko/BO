import random

def aliencolor():
    aliencolor:list[str] = ["verde", "giallo", "rosso"]
    col:list[str] = []
    risultati:list[str] = []
    
    for i in range(10):

        bo:str = random.choice(aliencolor)
        if bo == "verde":
            risultati.append("+5")
        else:
            risultati.append("+10")
        col.append(bo)
    
    print(col)
    print(risultati)


aliencolor()

"""""
Metodo più lento

        bo:int = random.randint(1, len(aliencolor))
        if bo == 1:
            risultati.append("+5")
        else:
            risultati.append("+10")
        numeri.append(bo)

"""""