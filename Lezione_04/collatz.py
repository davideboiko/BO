import matplotlib.pyplot as plt

def Collatz(n: int) -> list[int]:


    numeri:list[float] = [n]  

    while n != 1:
        if n % 2 == 0:
            n = n // 2

        else:
            n = (n * 3) + 1
        numeri.append(n)
        print(n)
    return numeri

numeri:list[float] = Collatz(7)

plt.plot(numeri, marker='o')
plt.title('Sequenza di Collatz per n = 7')
plt.xlabel('Passi')
plt.ylabel('Valore')
plt.grid(True)
plt.show()
