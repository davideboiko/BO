def tre(n:int):

    tre:list = []
    for i in range(3, n + 1, 3):
        print(i)
        tre.append(i)
    print(tre)

tre(30)