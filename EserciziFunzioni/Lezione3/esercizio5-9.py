import random

def helloadmin2():
    name:list[str] = []
    if not name:
        print("We need to find some users!")
    else:
        for i in range(10):
        
            bo:str = random.choice(name)

            if bo == "admin":
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Hello {bo}, thank you for logging in again")
helloadmin2()


"""""
Ricordarsi: if not "variabile":
"""""