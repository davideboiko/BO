class Persona:

    def __init__(self):
        self.name = name= ""
        self.lastname = lastname= ""
        self.age = age= 0



    def displaydata(self) -> None:
        print(f"Nome: {self.name} \nCognome: {self.lastname}\nEta: {self.age} ")

    def setName(self, name:str)-> None:
        self.name = name

    def setLastName(self, lastname:str)-> None:
        self.lastname = lastname

    def setAge(self, age:int)-> None:
        if age < 0 or age >100:
            self.age = "morto"
        else:
            self.age = age


    def getName(self) -> str:
        return self.name
    
    def getLastName(self) -> str:
        return self.lastname
    
    def getAge(self) -> int:
        return self.age

p:Persona = Persona()

p.setName("Davide")
p.setLastName("Boyko")
p.setAge(20)

p.displaydata()

print("\n-------------\n")
print(p.getName(), p.getLastName(), p.getAge())