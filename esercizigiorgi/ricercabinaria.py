def ricerca_binaria(lista_n, n):
    lista_n:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    mid: int = len(lista_n) // 2

    if lista_n[mid] == n:

        return True
    
    if lista_n[mid] > n:

        i:int = 0
        j:int = mid

        return ricerca_binaria(lista_n[i:j], n)

    else:

        j:int = mid
        
        return ricerca_binaria(lista_n[i:j], n)
