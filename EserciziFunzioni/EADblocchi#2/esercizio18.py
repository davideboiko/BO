import random


def num_random():
     
    num_random:list[int] = []
    for i in range(1, 11):
     
     i:int = random.randint(1, 100)
     num_random.append(i)
    
    print(num_random)

som:int = 0

for i in num_random():
   if i % 2 == 0:
      som 





