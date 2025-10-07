"""""
Nel corridoio successivo le trappole scattano sui duplicati: lascia passare solo le prime impronte usando `dedup_stable(nums)`,
 che restituisce una nuova lista con la prima comparsa di ogni valore mantenendo l'ordine della lista originale. 
 Mantieni la firma e scivola oltre i test.
"""""

def dedup_stable(nums: list[int]) -> list[int]:
    num = []
    for i in nums:
        if i not in num:
           num.append(i)
    print(num)
    return num
dedup_stable([1, 2, 5, 3, 2, 4, 1, 5])