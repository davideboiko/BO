from functools import reduce

numeri:list[int] = [2, 3, 4]
prodotto:list[int] = reduce(lambda x, y: x * y, numeri)
print(prodotto)