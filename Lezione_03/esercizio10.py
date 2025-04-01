x = int(input("Inserisci il giorno: "))
y = int(input("Inserisci il mese: "))

festa:tuple[int, int] = (x, y)

match festa:
    case (1, 1):
        print("Il 01/01 è Capodanno")
    case (14, 2):
        print("Il 14/02 è San Valentino")
    case (2, 6):
        print("Il 02/06 è la Festa della Repubblica Italiana")
    case (15, 8):
        print("Il 15/08 è Ferragosto")
    case (31, 10):
        print("Il 31/10 è Halloween")
    case (25, 12):
        print("Il 25/12 è Natale")
    case _:
        print("Nessuna festività importante in questa data.")