def calcola_stipendio(ore_lavorate: int) -> float:
    ore_str:int = ore_lavorate - 40
    stipendio:int = 0
    if ore_lavorate >= 40:
        stipendio = (ore_lavorate * 10) + (ore_str * 15)
    elif ore_lavorate <= 40:
        stipendio = ore_lavorate * 10
    return stipendio

	
print(calcola_stipendio(40))

print(calcola_stipendio(30))

print(calcola_stipendio(45))

print(calcola_stipendio(60))

print(calcola_stipendio(0))
