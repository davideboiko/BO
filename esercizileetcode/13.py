#Roman to Integer


def romaninteger(s:str) -> int:

    som:int = 0
    valori = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in s:
        if i == valori:
            som += valori[value] 

