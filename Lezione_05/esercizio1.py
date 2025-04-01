"""""
som0:int = 0
for i in range(1,11):
    som0 = som0 + i
print(f"La prima somma è: {som0}")

som1:int = 0
for i in range(20,38):
    som1 = som1 + i
print(f"La seconda somma è: {som1}")

som2:int = 0
for i in range(35,50):
    som2 = som2 + i
print(f"La terza somma è: {som2}")


def som(a:int, b:int):
    somma:int = 0

    for i in range(a, b+1):
        somma = somma + i
    return somma
print(f"La prima somma è: {som(1, 10)}")
print(f"La seconda somma è: {som(20, 37)}")
print(f"La terza somma è: {som(35, 49)}")



def subtract(c:int, d:int):
    sub:int = c - d

    return sub
print(f"Subtract: {subtract(20, 10)}")



# define a function returning multiple values(returning a tuple)
def operations(a: int, b: int) -> tuple[int, int]:
 sum_result:int = a + b
 diff_result:int = a - b

 # Returns a tuple with two values
 return sum_result, diff_result

# Assigns values to two variables
sum_value, diff_value = operations(10, 5)
print("Sum:", sum_value) # Output: Sum: 15
print("Difference:", diff_value) # Output: Difference: 5
print(type(operations(10,5)))


def check_value(a: int):
 b:int = 10
 if a > b:
  print("a è maggiore di b")
 elif a == b:
  print("sono uguali")
 else:
  print("a è minore di b")
 
print(check_value(8))


def check_lenght(a: str):

 if len(a) > 10:
  print("bigger")
 elif len(a) == 10:
  print("equal")
 else:
  print("smaller")
 
print(check_lenght("ciaocomest"))


def print_numbers(a: int):
    for i in range(a):
        print(i)
print(print_numbers(5))


def check_each(a: int):
    for i in range(a):
        print(i)
        if i > 5:
            print("bigger")
        elif i == 5:
            print("equal")
        else:
            print("smaller")
print(check_each(10))

"""""

def add_one(a:int):

    return a = a + 1


