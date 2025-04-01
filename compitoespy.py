"""""
#esercizio 1

parola:str = ""

while parola != "fine":
    parola:str = input("Inserire una parola: ")

    if parola[0] == parola[-1]:
        print("pisda")
    else:
        print("no pisda")
"""""
#esercizio 2

"""""
#Parte 1

#esercizio 1


x = float(input("inserisci un numero con la virgola: "))
y:float = 1.0 / x
prodotto:float = x * y
print(x)
print(y)
print(prodotto)
print(prodotto - x)


#esercizio 2

x = float(input("inserisci un numero con la virgola: "))
y:float = x%2.0

print(x)
print(y)


#esercizio 3

x = int(input("inserisci un numero con la virgola: "))
y = int(input("inserisci un numero con la virgola: "))
z = int(input("inserisci un numero con la virgola: "))

media = (x + y + z)/3
print(media)


#esercizio 5


gradiFahrenheit = int(input("inserisci temperatura: "))

gradiCelsius:float = 5*(gradiFahrenheit-32)/9

print(gradiCelsius)


#esercizio 6

#Fine Parte 1
#Parte 2


#esercizio 1

Eric:str = "Hello Eric, would you like to learn some Python today?"

print(f"Message for Eric:{Eric}")


#esercizio 2

name:str = input("inserisci un nome: ")

print(name.lower())
print(name.upper())
print(name.title())


#esercizio 3

name:str = input("inserisci un nome di un autore: ")

quote = {"Albert Einstein": "A person who never made a mistake never tried anything new",
          "Dalai Lama": "Lo scopo della nostra vita è essere felici",
          "Mahatma Gandhi": "Sii il cambiamento che vuoi vedere nel mondo"} 

if name == "Albert Einstein":
    print(f"Albert Einstein once said, \"{quote['Albert Einstein']}\"")
elif name == "Dalai Lama":
    print(f"Dalai Lama once said, \"{quote['Dalai Lama']}\"")


#esercizio 4


names = ["Luca", "Maria", "Giulia", "Marco"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])


#esercizio 5

names = ["Luca", "Maria", "Giulia", "Marco"]

print(f"Ciao {names[0]}, spero tu stia bene!")
print(f"Ciao {names[1]}, spero tu stia bene!")
print(f"Ciao {names[2]}, spero tu stia bene!")
print(f"Ciao {names[3]}, spero tu stia bene!")

#esercizio 6


mezzi = ["Ferrari", "Pagani", "Lambo"]

print(f"Mi piacerebbe possedere una {mezzi[0]}.")
print(f"Mi piacerebbe possedere una {mezzi[1]}.")
print(f"Mi piacerebbe possedere una {mezzi[2]}.")

#esercizio 7

listaa = ["Luca", "Maria", "Giulia"]


print(f"Ao {listaa[0]}, vie a cena. Sbrigate!")
print(f"Ao {listaa[1]}, vie a cena. Sbrigate!")
print(f"Ao {listaa[2]}, vie a cena. Sbrigate!")

#esercizio 8

listaa = ["Luca", "Maria", "Giulia"]


print(f"Ao {listaa[0]}, vie a cena. Sbrigate!")
print(f"Ao {listaa[1]}, vie a cena. Sbrigate!")
print(f"Ao {listaa[2]}, vie a cena. Sbrigate!")

icnpv = "Giulia"
print(f"Sfortunatamente, {icnpv} non può partecipare alla cena.")
listaa[2] = "Camilla"

print(f"Ao {listaa[0]}, vie a cena. Sbrigate!")
print(f"Ao {listaa[1]}, vie a cena. Sbrigate!")
print(f"Ao {listaa[2]}, vie a cena. Sbrigate!")

#esercizio 9

listaa = ["Luca", "Maria", "Giulia"]

print("Posso invitare più persone")

listaa.insert(0, "Franco")
listaa.insert(2, "Pietro")
listaa.append("Elon")



primo:set[int] = {1,5,7,9} 
secondo:set[int] = {2,3,6,8} 

primo.update(secondo)

print(primo)

primo.union(secondo)

print(primo)


mydict:dict = {"key1":"value1","key2":"value2","key3":"value3",}

for key in mydict:
    print(key)


for key in mydict:
    print(mydict[key])

for key,values in mydict.items():
    print(f"chiave: {key}, valore: {values}")





pos = input("inserisci la posizione: ")
if pos == "1st" or pos == "1":
    print("1st")
elif pos == "2nd" or pos == "2":
    print("2nd")
elif pos == "3rd" or pos == "3":
    print("3rd")
else:
    print(f"{pos}th")

"""""
"""""
pos = int(input("inserisci la posizione: "))

match pos:
    case 1:
        print("1st")
    case pos if pos > 1 and pos < 3:
        print("2nd")
    case 3:
        print("3rd")
    case _:
        print(f"{pos}th")


nel case l'or si scrive con la |
case 1 | 2:
    print("1st")

si possono usare gli if
case n if n > 0 and n%2==0:
    print("bo")

nel caso di due variabili
match bo, age:
    case("g", 6):
        print("non lo so")

#Esercizio 3C-00A

num = int(input("inserisci la posizione: "))

match num:
    case 1:
        print("Congratulazioni")
    case 2:
        print("Wow! Gemelli!")
    case 3:
        print("Wow! Tre!")
    case 4:
        print("Mamma mia Quattro! Wow!")
    case 5:
        print("ncredibile! Cinque!")
    case _:
        print(f"Non ci credo! {num} bambini")


#Esercizio 3C-00B


nome:str = input("inserisci Nome: ")
g:str = input("Inserire gender. Digitare m per maschio e f per femmina: ")

match g:
    case g if g == "m":
        print(f"Nome: {nome}")
        print(f"Gender: Maschio")

    case g if g == "f":
        print(f"Nome: {nome}")
        print(f"Gender: Femmina")
    case _:
        print(f"Nome: {nome}")
        print(f"Mi dispiace {nome}, non e' possibile procedere con la generazione di un documento di identità!")

#Esercizio 3C-1

voto = int(input("inserisci la valutazione: "))

match voto:
    case 10:
        print("Eccellente")
    case 8 | 9:
        print("Molto buono")
    case 6 | 7:
        print("Sufficiente")
    case 4 | 5:
        print("Insufficiente")
    case 1 | 2 | 3:
        print("Gravemente insufficiente")
    case _:
        print(f"Voto non valido")

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


#Esercizio 3C-3

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

#Esercizio 3C-4

"""""

#Esercizio 3C-5



