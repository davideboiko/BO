import random

class Creatura:
    def __init__(self, nome: str):
        self.nome = nome

    def setNome(self, nome):
        if isinstance(nome, str) and nome.isalpha():
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def getNome(self):
        return self.__nome

    def __str__(self):
        return f"Creatura: {self.__nome}"


class Alieno(Creatura):

    def __init__(self, nome: str, matricola:int, munizioni:list):
        super().__init__(nome)
        self.__matricola = matricola
        self.__munizioni = munizioni

    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)

    def getMatricola(self):
        return self.__matricola

    def __setMunizioni(self):
        self.__munizioni = [i**2 for i in range(16)]

    def getMunizioni(self):
        return self.__munizioni

    def __str__(self):
        return f"Alieno: {self.getNome()}"
    

class Mostro(Creatura):

    def __init__(self, nome, urlo_vittoria:str, gemito_sconfitta:str, assalto:list):
        super().__init__(nome)
        self.urlo_vittoria = urlo_vittoria
        self.gemito_sconfitta = gemito_sconfitta
        self.assalto = assalto

    def setUrlo_Vittoria(self, urlo_vittoria:str):

        if isinstance(urlo_vittoria, str) and len(urlo_vittoria.strip()) > 0:
            self.__urlo_vittoria = urlo_vittoria

        else:

            self.__urlo_vittoria = "GRAAAHHH"

    def getUrlo_Vittoria(self):

        return self.urlo_vittoria
    
    def setGemito_Sconfitta(self, gemito_sconfitta:str):

        if isinstance(gemito_sconfitta, str) and len(gemito_sconfitta.strip()) > 0:
            self.__gemito_sconfitta = gemito_sconfitta

        else:

            self.__gemito_sconfitta = "Uuurghhh"

    def getGemito_Sconfitta(self):

        return self.__gemito_sconfitta

    def setAssalto(self, assalto:int):

        self.__assalto = random.sample((0, 101), 15)

    def getAssalto(self):

        return self.__assalto
    
    def __str__(self):
        return f"Mostro: {self.getNome()}"
    

def paroUguali():
    a:list[int] = [random.randint(1, 10) for _ in range(10)]
    b:list[int] = [random.randint(1, 10) for _ in range(10)]

    print(a)
    print(b)

    c:list[int] = []

    for i,j in zip(a,b):

        if i%2 == 0 and j%2 == 0:

            c.append(-1)
        
        else:

            c.append(0)

    print(c)

paroUguali()

    
        
