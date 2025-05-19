def fetta():
    numeri:list = []
    
    for i in range(1, 11):
        numeri.append(i)
    print(numeri)
    
    print(f"I primi tre elementi della lista sono: {numeri[0:3]}")
    meta:int = len(numeri) // 2
    print(f"I primi tre elementi della lista sono: {numeri[meta-1:meta+2]}")

    print(f"I primi tre elementi della lista sono: {numeri[-3:]}")

fetta()