import random

def fasivita():
    numeri:list[int] = []
    
    for i in range(10):

        bo:int = random.randint(1, 100)
        if bo < 2:
            print("La persona è un baby")
        elif bo > 2 and bo < 4:
            print("La persona è un toddler")
        elif bo > 4 and bo < 13:
            print("La persona è un kid")
        elif bo > 13 and bo < 20:
            print("La persona è un teenager")
        elif bo > 20 and bo < 65:
            print("La persona è un adult")
        elif bo > 65:
            print("La persona è un elder")
            
        
        numeri.append(bo)
        
    print(numeri)

fasivita()