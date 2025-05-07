def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:

    ore_dal_mezzogiorno = ore % 12
    if ore == 12:
        ore_dal_mezzogiorno = 12
    return ore_dal_mezzogiorno * 3600 + minuti * 60 + secondi

def time_difference(ore1: int, min1: int, sec1: int, ore2: int, min2: int, sec2: int) -> int:

    tempo1 = seconds_since_noon(ore1, min1, sec1)
    tempo2 = seconds_since_noon(ore2, min2, sec2)
    return abs(tempo2 - tempo1)


 	

print(time_difference(1, 0, 0, 3, 15, 30))
print(time_difference(11, 59, 59, 2, 0, 0))
print(time_difference(0, 0, 0, 12, 0, 0))
print(time_difference(9, 0, 0, 11, 0, 0))