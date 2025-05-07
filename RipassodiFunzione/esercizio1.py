def numero_magico(num: int) -> bool:
    if num % 4 == 0 and num % 6 != 0:
        return True
    else:
        return False

print(numero_magico(8))
print(numero_magico(12))
print(numero_magico(16))
print(numero_magico(24))
print(numero_magico(28))