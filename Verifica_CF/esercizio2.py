"""""
Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista. Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.
Il tuo compito è individuare i numeri mancanti.
Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.
For example:
Test 	Result

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
[5, 6]
"""""
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n:int = len(nums)
    num_mancanti:list = []
    for i in range(1, n + 1):
        if i not in nums:
            num_mancanti.append(i)
    return num_mancanti

# Test della funzione
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disappeared_numbers([1,8,9,150,9,2189,2,82,3,3,3]))
 	

print(find_disappeared_numbers([1,8,9,150]))