def converter():
    bo1:tuple = [('a', 2), ('b', 3), ('a', 4), ('c', 1), ('b', 2)]
    bo:dict = {}

    for key, value in bo1:
        if key in bo:
            bo[key] += value
        else:
            bo[key] = value

    return f"{bo1} \n {bo}"

print(converter())



"""""
for element in num:
        key, value = element[0], element[1]
        if key in bo:
            bo[key] += value
        else:
            bo[key] = value  
    return bo

"""""