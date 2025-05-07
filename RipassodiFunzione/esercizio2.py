def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    diz: dict[str, list[int]] = {}
    for key, value in tuples:
        if key in diz:
            diz[key].append(value)
        else:
            diz[key] = [value]
    return diz

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([('a', 1)]))
print(lista_a_dizionario([]))
print(lista_a_dizionario([('b', 2), ('b', 3)]))
print(lista_a_dizionario([('c', 1), ('b', 2), ('c', 3), ('c', 4)]))