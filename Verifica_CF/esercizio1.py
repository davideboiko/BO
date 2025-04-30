"""""
Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

    tutti i numeri pari vengano prima di tutti i numeri dispari;

    l’ordine relativo tra pari e dispari va mantenuto;

    l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

For example:
Test 	Result

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
[6, 8, 4, 3, 1, 7]
"""""
def even_odd_pattern(numbers:list[int]) -> list[int]:
    num_pari = []
    num_disp = []
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            num_pari.append(numbers[i])
        else:
            num_disp.append(numbers[i])
    numbers = num_pari + num_disp
    return numbers

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))