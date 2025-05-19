def pizza():
    pizza:list[str]  = ["margherita", "diavola", "bo"]


    for i in pizza:
       print(i)
    for i in pizza:
       print(f"I like {i} pizza")

    print(f"I love {pizza[0]} pizza")
    print(f"I love {pizza[1]} pizza")
    print(f"I love {pizza[2]} pizza")

pizza()