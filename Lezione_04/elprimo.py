#capire se è primo 


def elprimo(num:int):

    for i in range(2, num + 1):
        if num % i == 0:
            return False
    return True
 

print(elprimo(7))