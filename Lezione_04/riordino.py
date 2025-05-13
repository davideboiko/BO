# riordinare i numeri dal più piccolo al più grande
import random


num:list[int] = []

for i in random.sample(range(1, 101), 10):
    num.append(i)
print(num)
