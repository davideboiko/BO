def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    diz: dict[str, list[int]] = {}

    for voto in voti:

        name = voto["nome"]
        valutazioni = voto["voto"]

        if name in diz:
            diz[name].append(valutazioni)
        else:
            diz[name] = [valutazioni]
    return diz
    
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([{'nome': 'Alice', 'voto': 100}]))
print(aggrega_voti([{'nome': 'Bob', 'voto': 75}, {'nome': 'Bob', 'voto': 85}]))
print(aggrega_voti([]))
print(aggrega_voti([{'nome': 'Carl', 'voto': 60}, {'nome': 'Carl', 'voto': 70}, {'nome': 'Carl', 'voto': 80}]))