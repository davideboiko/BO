#Esercizio 3C-2 (non funzionante)

voto = int(input("inserisci la valutazione: "))

match voto:

    case range(106,111):
        print("4.0")
    case range(101,106):
        print("3.3")
    case range(91,96):
        print("3.0")
    case range(86,91):
        print("2.7")
    case range(81, 86):
        print("2.3")
    case range(76, 81):
        print("2.0")
    case range(70, 76):
        print("1.7")
    case range(66, 70):
        print("1.0")
    case _:
        print(f"Voto non valido")


#Esercizio 3C-2 (funzionante)

voto = int(input("Inserisci la valutazione: "))

match voto:
    case voto if 106 <= voto <= 110:
        print("GPA 4.0")
    case voto if 101 <= voto <= 105:
        print("GPA 3.7")
    case voto if 96 <= voto <= 100:
        print("GPA 3.3")
    case voto if 91 <= voto <= 95:
        print("GPA 3.0")
    case voto if 86 <= voto <= 90:
        print("GPA 2.7")
    case voto if 81 <= voto <= 85:
        print("GPA 2.3")
    case voto if 76 <= voto <= 80:
        print("GPA 2.0")
    case voto if 70 <= voto <= 75:
        print("GPA 1.7")
    case voto if 66 <= voto <= 69:
        print("GPA 1.0")
    case _:
        print(f"Voto non valido")
