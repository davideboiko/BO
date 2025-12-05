from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id:str, nome:str, age_years:int, weight_kg:float):

        self.id = id
        self.nome = nome
        self.age_years = age_years
        self.weight_kg = weight_kg
    
    @abstractmethod
    def species(self) -> str:
        return
    
    @abstractmethod
    def daily_food_grams(self) -> float:
        return
    
    def info(self) -> dict:
        return { "id": self.id,
                 "nome": self.nome,
                 "species": self.species(),
                   "age_years": self.age_years,
                   "weight_kg": self.weight_kg
                   }
    
    def bmi_like(self) -> float: 
        return weight_kg / (age_years + 1)
    
class Dog(Animal):
    def __init__(self, id:str, nome:str, age_years:int, weight_kg:float, breed:str, is_trained:bool):
        super().__init__(id, nome, age_years, weight_kg)
        
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> float:
        return 200 + self.age_years * 50
    
    def info(self) -> dict:
        base_info = super().info()
        base_info.update({ 
                 "dreed": self.breed,
                 "is_trained": self.is_trained
                   })
        return base_info
    
class Cat(Animal):
    def __init__(self, id:str, nome:str, age_years:int, weight_kg:float, indoor_only:bool, favorite_toy:str):
        super().__init__(id, nome, age_years, weight_kg)

        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy
    
    def species(self) -> str:
        return "cat"
    
    def daily_food_grams(self) -> float:
        return 100 + self.age_years * 30
    
    def info(self) -> dict:
        base_info = super().info()
        base_info.update({
            "indoor_only": self.indoor_only,
            "favorite_toy": self.favorite_toy
        })
        return base_info
    
class Shelter:
    def __init__(self, animals: dict[str, Animal], adoptions: dict[str, str]):
        self.animals = animals
        self.adoptions = adoptions

    def add(self, animal: Animal):
        # Se l'ID esiste già, solleviamo un errore (come volevi fare tu)
        if animal.id in self.animals:
            raise KeyError("Il codice si trova già nella lista.")

        self.animals[animal.id] = animal

    def get(self, animal_id: str):
        if animal_id not in self.animals:
            raise KeyError(f"Non esiste un animale con il codice {animal_id}")
        return self.animals[animal_id]

    def list_all(self):
        # Restituiamo la lista dei dizionari info()
        return [animal.info() for animal in self.animals.values()]

    def is_adopted(self, animal_id: str) -> bool:
        # True se l'animale risulta adottato
        return animal_id in self.adoptions

    def set_adopted(self, animal_id: str, adopter_name: str):
        if animal_id not in self.animals:
            raise KeyError(f"Non esiste un animale con il codice {animal_id}")
        self.adoptions[animal_id] = adopter_name


    


 
