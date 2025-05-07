from persona import Persona
from studente import Studente

#creo un oggetto della classe persona

fm: Persona = Persona("Davide", "Boyko", 20)

#visualizza le informazioni relative allo studente

print(fm)

studente1: Studente = Studente("Davide", "Boyko", 20, "123456")

print(studente1)

if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe studente ")

if isinstance(studente1, Persona):
    print("\nstudente1 è anche istanza della classe persona ")

if isinstance(fm, Persona):
    print("\nfm è anche istanza della classe persona ")
if isinstance(fm, Studente):
    print("\nfm è anche istanza della classe studente ")
else:
    print("\nfm non è anche istanza della classe studente")


   # controllare che la classe studente sia sottoclasse di persona
if issubclass(Studente, Persona):
    print("\nla classe studente è sottoclasse di persona")
