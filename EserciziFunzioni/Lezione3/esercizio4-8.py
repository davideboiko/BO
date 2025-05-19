def cubi():
    numeri:list = []
    cubi:list = []
    for i in range(1, 11):
        numeri.append(i)
    print(numeri)
    for i in numeri:
        i = i ** 3
        cubi.append(i)
    print(cubi)
cubi()