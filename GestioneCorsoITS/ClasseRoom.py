class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id





























































class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2  # Supponiamo che ogni posto abbia 2 m² di area

    def get_id(self):
        return self.id

    def get_floor(self):
        return self.floor

    def get_seats(self):
        return self.seats

    def get_area(self):
        return self.area


class Building:
    def __init__(self, name: str, address: str, floors: tuple):
        self.name = name
        self.address = address
        self.floors = floors  # Tuple (minimo piano, massimo piano)
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room: Room):
        # Aggiungi la stanza se il piano è valido
        if room.get_floor() < self.floors[0] or room.get_floor() > self.floors[1]:
            return
        # Aggiungi la stanza solo se non esiste già una stanza con lo stesso ID
        for existing_room in self.rooms:
            if existing_room.get_id() == room.get_id():
                return
        self.rooms.append(room)

    def area(self):
        # Calcola l'area totale dell'edificio
        return sum(room.get_area() for room in self.rooms)


# Creazione di stanze
room1 = Room(id="Room1", floor=1, seats=15)
room2 = Room(id="Room2", floor=5, seats=20)
room3 = Room(id="Room3", floor=11, seats=10)  # Questo piano è fuori dal range

# Creazione di un edificio
building = Building(name="Test Building", address="123 Test St", floors=(1, 10))

# Aggiunta delle stanze all'edificio
building.add_room(room1)  # Aggiunta Room1
building.add_room(room3)  # Tentativo di aggiungere Room3 (piano non valido)
building.add_room(room1)  # Tentativo di aggiungere Room1 (duplicato)
building.add_room(room2)  # Aggiunta Room2
