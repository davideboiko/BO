def divisione():
    num: list[int] = [1, 2, 3, 4, -1, -2, -3, -4, 55, -66]
    bo: dict[str, list[int]] = {"positivo": [], "negativo": []}

    for i in num:
        if i >= 0:
            bo["positivo"].append(i) 
        else:
            bo["negativo"].append(i)

    return bo

print(divisione())

            



