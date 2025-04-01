

class Persona:


#Di una persona dobbiamo sapere delle informazioni
#Queste informazioni vengono chiamate attributi
#Le informazioni saranno -nome -cognome -età

#Costruzione della Classe Persona


#self.name:str (attributo stringa)
#self.lastname:str
#self.age:int (attributo intero)



#Costruttore della classe persona
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age



    def displaydata(self) -> None:
        print(f"Nome {self.name} \nCognome {self.lastname}\nEta {self.age} ")

p:Persona = Persona("bo","boo", 22)

print(p)

p.displaydata()