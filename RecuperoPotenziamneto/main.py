from esercizio1 import Frazione

f1 = Frazione(3, 4)
print(f1)               # Output: 3 / 4
print(f1.value())       # Output: 0.75

f2 = Frazione("a", 0)   # Input invalido
print(f2)               # Output: 13 / 5
print(f2.value())       # Output: 2.6