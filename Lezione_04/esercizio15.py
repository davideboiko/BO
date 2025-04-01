pizza:list[str] = ["margherita",
                     "diavola",
                       "bo"]
friend_pizzas:list[str] = ["margherita",
                             "diavola",
                               "bo"]

pizza.append("capricciosa")
friend_pizzas.append("blyat")

print("My favorite pizza are: ")
for i in pizza:
    print(i)

print("My friend’s favorite pizzas are:")
for i in friend_pizzas:
    print(i)