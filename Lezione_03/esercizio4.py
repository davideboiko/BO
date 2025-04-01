mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]  
rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]  
uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco"]  
pesci:list[str] = ["squalo", "trota", "salmone", "carpa"]  


animale:str = input("Inserire animale:")

match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi")
    case animale if animale in rettili:
        print(f"{animale} appartiene alla categoria dei Rettili")
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria dei Uccelli")
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria dei Pesci")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}")