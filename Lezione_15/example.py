PATH:str = "Lezione_15/example.txt"
dome:str = "r"
encoding:str = "utf-8"

file = open(PATH)
output:str = file.read()
#output:str = file.write("ciao come stai") va a sovrascrivere
#output:str = file.write(output) fa scrivere da terminale
print(output)
file.close()


"""""
file = open("Lezione_15/example.txt", "a")

try:
    pass
except Exeption as e:
    pass
finally:
    file.close()

mode:
    'r' (lettura)

    'w' (scrittura, sovrascrive)

    'a' (append, aggiunge in fondo)

    'r+' (lettura e scrittura)

    'b' (modalità binaria, es. 'rb' o 'wb')
"""""