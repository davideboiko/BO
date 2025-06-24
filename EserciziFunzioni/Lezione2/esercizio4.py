import random


"""""
def esercizio4(x:str):

    for i in x:
        print(f"{i}")

esercizio4("2024")

"""""

    
def paroUguali():
    a:list[int] = [random.randint(1, 10) for _ in range(10)]
    b:list[int] = [random.randint(1, 10) for _ in range(10)]

    print(a)
    print(b)

    c:list[int] = []

    for i,j in zip(a,b):

        if i%2 == 0 and j%2 == 0:

            c.append(-1)
        
        else:

            c.append(0)

    print(c)

paroUguali()


