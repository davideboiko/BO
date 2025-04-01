#esercizio 3

name:str = input("inserisci un nome di un autore: ")

quote = {"Albert Einstein": "A person who never made a mistake never tried anything new",
          "Dalai Lama": "Lo scopo della nostra vita è essere felici",
          "Mahatma Gandhi": "Sii il cambiamento che vuoi vedere nel mondo"} 

if name == "Albert Einstein":
    print(f"Albert Einstein once said, \"{quote['Albert Einstein']}\"")
elif name == "Dalai Lama":
    print(f"Dalai Lama once said, \"{quote['Dalai Lama']}\"")
