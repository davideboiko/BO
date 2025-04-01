def frequency_dict(elements: list) -> dict:
    num = {} 

    for value in elements:
        if value in num:
            num[value] += 1
        else:
            num[value] = 1
    return num

print(frequency_dict(['mela', 'banana', 'mela', "arancia", "arancia"]))