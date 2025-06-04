def condizione(x:bool, y:bool, z:bool):
    if x == True and (y == True or z == True):
        return "Azione permessa"
    else:
        return "Azione negata"


print(condizione(True, True, False))   # Azione permessa
print(condizione(True, False, True))   # Azione permessa
print(condizione(True, False, False))  # Azione negata
print(condizione(False, True, True))   # Azione negata

"""""
return "Azione permessa" if x and (y or z) else "Azione negata"
"""""