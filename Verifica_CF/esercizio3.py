"""""
Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

For example:
Test 	Result

print(somma_elementi([1,1,1],[1,1,1])) [2, 2, 2]
"""""
def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    for i in range(len(x)):
        x[i] += y[i] 

    return x
x = [1, 2, 3]
y = [4, 5, 6]
print(somma_elementi(x, y))