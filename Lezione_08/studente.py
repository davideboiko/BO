from persona import Persona


class Studente(Persona):

#Inizializzare la classe Persona richiamando il metodo init della superclasse

    def __init__(self, name: str, lastname: str, age: int, matricola: str):
        super().__init__(name, lastname, age)


#Inizializzazione oggetto classe
        self.setMatricola(matricola)

    def setMatricola(self, matricola: str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("La matricola non può essere rappresentata da una stringa vuota")
    
    def getMatricola(self) -> str:
        return self.matricola
    
    def getLastName(self) -> str:
        return self.lastname
    
    def __str__(self) -> str:
        return f"\nNome: {self.name}\nCognome:{self.getLastName()}\nMatricola: {self.getMatricola()} "