oggetti:list[str] = []

for i in range(3):
    bo:str = input("inserire parole:")
    oggetti.append(bo)

match oggetti:

    case ["penna", "matita", "quaderno"]:
        print(oggetti)
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print(oggetti)
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print(oggetti)
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print(oggetti)
        print("Dispositivi elettronici")
    case _:
        print(oggetti)
        print("Categoria sconosciuta")