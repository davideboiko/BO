testa:int = 0
croce:int = 0
for i in range(1,9):
    moneta = input(f"Lancio {i} : ").lower()
    match moneta:
        case 't':
            testa += 1
        case 'c':
            croce += 1
        case _:
            print("Inserisci o 't' o 'c'.")

p_testa = (testa / 8) * 100


print(f"Numero totale di teste: {testa}")
print(f"Numero totale di croci: {croce}")
print(f"Percentuale 'testa': {p_testa:.2f}%")
print(f"Percentuale 'croce': {100-p_testa:.2f}%")


















"""""

    if moneta != "t" or moneta != "T" or moneta != "c" or moneta != "C":
        moneta:str = input("Lancio: ")
    else:
        print(moneta)
        m.append(moneta)

"""""