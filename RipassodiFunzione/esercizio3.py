def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    bo:list[int] = [] 
    for i in lista:
        if i in da_rimuovere and da_rimuovere[i] > 0:
            da_rimuovere[i] -= 1
        else:
            bo.append(i)
    
    return bo

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))

print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))

print(rimuovi_elementi([4, 5, 6], {1: 3}))

print(rimuovi_elementi([], {2: 1}))