from abc import ABC, abstractmethod
from math import ceil

class Ride(ABC):
    def __init__(self, id:str, name:str, min_high_cm:int):
        self.id = id
        self.name = name
        self.min_high_cm = min_high_cm
    
    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod 
    def base_wait(self) -> int:
        pass

    @abstractmethod 
    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "nim_high_cm": self.min_high_cm,
            "category": self.category()
            }
    
    def wait_time(self, crowd_factor: float = 1.0) -> float:
        if crowd_factor < 0:
            raise ValueError("crowd_factor non può essere negativo")
        return ceil(self.base_wait() * crowd_factor)

class RollerCoaster(Ride):
    def __init__(self, id:str, name:str, min_high_cm:int, inversions:int):
        super().__init__(id, name, min_high_cm)
        self.inversions = inversions

    def category(self) -> str:
        return "roller_coaster"
    
    def base_wait(self) -> int:
        return 40
    
    def info(self):
        data = super().info()
        data["inversions"] = self.inversions
        return data 

class Carusel(Ride):
    def __init__(self, id:str, name:str, min_high_cm:int, animals:list[str]):
        super().__init__(id, name, min_high_cm)
        self.animals = animals
    
    def category(self) -> str:
        return "family"
    
    def base_wait(self):
        return 10
    
    def info(self):
        data = super().info()
        data["animals"] = self.animals
        return data 

class Park():
    def __init__(self, rides: dict):
        self.rides: dict[str, Ride] = {}

    def add(self, ride:Ride) -> str:
        if ride.id in self.rides:
            return f"Errore: la giostra {ride.name} è già nella lista"
        
        self.rides[ride.id] = ride
        
        return f"La giostra {ride.name} è stata aggiunta con successo"
    
    def get(self, ride_id:int) -> Ride:
        
        if ride_id not in self.rides:
            raise KeyError(f"Non esiste una giosta con questo id {ride_id}")
        return self.rides[ride_id]
    
    def list_all(self) -> list[Ride]:
        return list(self.rides.values())