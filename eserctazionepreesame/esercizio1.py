def countwords(listastringhe:list[str]) -> dict[str:int]:
    conteggio:dict[str:int] = {}

    for stringhe  in listastringhe:
        parole = stringhe.split()

        for parola in parole:
            parla = parola.lower()

            if parola in conteggio:
                conteggio[parola] += 1

            else:
                conteggio[parola] = 1

    return conteggio
    
listastringhe = ["ciao mondo", "ciao a tutti", "mondo bello"]
risultato = countwords(listastringhe)
print(risultato)
