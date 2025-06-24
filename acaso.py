import random

class Creatura:
    def __init__(self, nome):
        self.setNome(nome)

    def setNome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def getNome(self):
        return self.__nome

    def __str__(self):
        return f"Creatura: {self.__nome}"

class Alieno(Creatura):
    def __init__(self):
        self.__setMatricola()
        self.__setMunizioni()
        nome = f"Robot-{self.__matricola}"
        super().__init__(nome)
        if not nome.startswith("Robot-") or not nome[6:].isdigit():
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self.setNome(f"Robot-{self.__matricola}")

    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self):
        self.__munizioni = [i*i for i in range(15)]

    def getMunizioni(self):
        return self.__munizioni

    def getMatricola(self):
        return self.__matricola

    def __str__(self):
        return f"Alieno: {self.getNome()}"

class Mostro(Creatura):
    def __init__(self, nome, urlo_vittoria, gemito_sconfitta):
        super().__init__(nome)
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self.__setAssalto()

    def __setVittoria(self, vittoria):
        self.__urlo_vittoria = vittoria if isinstance(vittoria, str) else "GRAAAHHH"

    def __setSconfitta(self, sconfitta):
        self.__gemito_sconfitta = sconfitta if isinstance(sconfitta, str) else "Uuurghhh"

    def __setAssalto(self):
        self.__assalto = random.sample(range(1, 101), 15)

    def getVittoria(self):
        return self.__urlo_vittoria

    def getSconfitta(self):
        return self.__gemito_sconfitta

    def getAssalto(self):
        return self.__assalto

    def __str__(self):
        nome = self.getNome()
        alternato = ''.join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(nome)])
        return f"Mostro: {alternato}"

def pariUguali(a, b):
    return [1 if a[i] % 2 == 0 and b[i] % 2 == 0 else 0 for i in range(min(len(a), len(b)))]

def combattimento(a, m):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Oggetti non validi per il combattimento.")
        return None
    print("\nCombattimento\n")
    risultato = pariUguali(a.getMunizioni(), m.getAssalto())
    if risultato.count(1) > 4:
        for _ in range(3):
            print(m.getVittoria())
        return m
    else:
        print(m.getSconfitta())
        return a

def proclamaVincitore(c):
    if isinstance(c, Alieno):
        print("\nI Robot hanno vinto!")
    elif isinstance(c, Mostro):
        print("\nI Mostri hanno vinto!")
    else:
        print("\nNessun vincitore.")
        return

    stringa = str(c)
    larghezza = len(stringa) + 10
    print("*" * larghezza)
    for i in range(5):
        if i == 2:
            spazi = (larghezza - len(stringa) - 2) // 2
            print("*" + " " * spazi + stringa + " " * (larghezza - len(stringa) - 2 - spazi) + "*")
        else:
            print("*" + " " * (larghezza - 2) + "*")
    print("*" * larghezza)

def main():
    alieno = Alieno()
    print(alieno)
    print("Munizioni:", alieno.getMunizioni())

    mostro = Mostro("gOrThOr", "GRAAAHHH", "Uuurghhh")
    print(mostro)
    print("Assalto:", mostro.getAssalto())

    vincitore = combattimento(alieno, mostro)
    if vincitore:
        proclamaVincitore(vincitore)

if __name__ == "__main__":
    main()
