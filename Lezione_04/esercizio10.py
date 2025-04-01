numeri:list[int]  = []

for i in range(3, 31,3):
    numeri.append(i)

print(numeri)


print(numeri[:3])

# Stampa tre elementi dal centro dell'elenco
numero_m = len(numeri) // 2
print(numeri[numero_m-1:numero_m+2])


print(numeri[-3:])