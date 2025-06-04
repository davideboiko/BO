som:int = 0


num:int =  int(input("Inserire un numero: "))

if 1 < num < 100:
    for i in range(1, num + 1):
        if i % 2 == 0:
            som += i
    print(som)
        
elif num < 0:
    print("Errore")

elif num > 100:
    for i in range(1, num + 1):
        if i % 2 == 1:
            som += i

    print(som)