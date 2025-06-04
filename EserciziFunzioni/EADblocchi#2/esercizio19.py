num: int = int(input("Inserire numero: "))


if num > 0 and num % 2 == 0:
    sum: int = 0
    for i in range(1, num +1):
        if i % 4 == 0:
            sum += i
    print(f"La somma dei numeri è {sum}")
elif num > 0 and num % 2 == 1:
    sum: int = 1
    for i in range(1, num +1, 2):
        sum *= i
    print(f"Il prodotto dei dispari {sum}")
elif num < 0:
    print("Errore")


    