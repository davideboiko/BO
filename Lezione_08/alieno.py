class Alieno:

    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)
        
    def setGalaxy(self, galaxy: str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("errore la galassia non puo essere una strigna vuota")
    
    def getGalaxy(self) -> str:
        return self.galaxy

    def speak(self) -> None:
        print(f"Hello my name is dhhbrtrjtby")
    
    def __str__(self):
        return f"Alieno proveniente dalla galassia {self.getGalaxy()} "