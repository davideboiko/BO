import random

def helloadmin():
    name:list[str] = ["Alessandro", "Davide", "Popa",
                       "Alessio", "Marco", "admin"]
    
    for i in range(10):
        
        bo:str = random.choice(name)

        if bo == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {bo}, thank you for logging in again")
helloadmin()
    

"""""
Metodo più lento

    for i in range(10):

        bo:int = random.randint(1, len(name))

        if bo == 5:
            print(f"Hello {name[5]}, would you like to see a status report?")
        elif bo == 4:
            print(f"Hello {name[4]}, thank you for logging in again")
        elif bo == 3:
            print(f"Hello {name[3]}, thank you for logging in again")
        elif bo == 2:
            print(f"Hello {name[2]}, thank you for logging in again")
        elif bo == 1:
            print(f"Hello {name[1]}, thank you for logging in again")

"""""