def ricerca_binaria(lista_n, n):
    if not lista_n:
        return False  # caso base: lista vuota

    mid = len(lista_n) // 2

    if lista_n[mid] == n:
        return True
    elif lista_n[mid] > n:
        return ricerca_binaria(lista_n[:mid], n)
    else:
        return ricerca_binaria(lista_n[mid+1:], n)


numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ricerca_binaria(numeri, 5))   # True
print(ricerca_binaria(numeri, 11))  # False
