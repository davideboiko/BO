import random

punteggio:int = 0

while punteggio < 100:
    d1:int = random.randint(1, 6)
    print(d1)
    d2:int = random.randint(1, 6)
    print(d2)
    som:int = d1 + d2
    print(som)


    if d1 % 2 == 0 and d2 % 2 == 0 and som > 8:
        punteggio += 100
        print(f"1: {punteggio}")
    elif (d1 == 6 or d2 == 6) or som == 7:
        punteggio += 10
        print(f"2: {punteggio}")
    else:
        punteggio = 0
        print(f"3: {punteggio}")




