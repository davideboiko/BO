mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]  
rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]  
uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco"]  
pesci:list[str] = ["squalo", "trota", "salmone", "carpa"]  
animal_type:list[str] = []  

animale:str = input("Inserire animale:")
habitat:str = input("Inserire habitat:")

match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi")
        animal_type.append(animale)
        print(animal_type)
    case animale if animale in rettili:
        animal_type.append(animale)
        print(f"{animale} appartiene alla categoria dei Rettili")
    case animale if animale in uccelli:
        animal_type.append(animale)
        print(f"{animale} appartiene alla categoria dei Uccelli")
    case animale if animale in pesci:
        animal_type.append(animale)
        print(f"{animale} appartiene alla categoria dei Pesci")
    case _:
        animal_type.append("unknown")
        print(animal_type)
        print(f"Non so dire in quale categoria classificare l'animale {animale}")

acqua:list[str] = [squalo, trota, salmone, carpa, balena, delfino, serpente, coccodrillo]
aria:list[str] = [aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino]
terra:list[str] = [serpente, lucertola, coccodrillo, cane, gatto, cavallo, elefante, leone]
