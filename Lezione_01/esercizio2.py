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

"""""

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
    print(f"chiave:{key}, valore:{values}")
