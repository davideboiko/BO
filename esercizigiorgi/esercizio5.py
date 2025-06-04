import random

def moltiplicazione(num:int):

    lista:list = []
    
    for i in range(10):
        bo:int = random.randint(1, 60)
        lista.append(bo)
    
    som:int = 1

    for i in lista:
        if i < num:
            som *= i
    return f"{lista} \n {som}" 



print(moltiplicazione(30))