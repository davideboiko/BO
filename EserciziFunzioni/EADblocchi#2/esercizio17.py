import random

som:int = 0

num_random:list[int] = []
for i in range(7):
     
    i:int = random.randint(1, 50)
    num_random.append(i)


    if i > 35 or i < 5:
        print("sta ceppa")
    elif 10 < i < 30:
        print("bo")
    som += i

print(num_random)


media:int = som / len(num_random)



