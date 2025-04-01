frase:str = input("Inserire una frase:")
match frase:
    case frase if frase[-1] == "?" and len(frase) % 2 == 0:
        print("ciao")
    case frase if frase[-1] == "?" :
        print("ciao2")
    case frase if frase[-1] == "!":
        print("ciao3")
    case _:
        print(f"Tu dici {frase}")