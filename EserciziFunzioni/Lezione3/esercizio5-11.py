def ordinalnum():
    num:list[int] = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    for i in num:
        if i == 1:
            print(f"{i}st")
        elif i == 2 :
            print(f"{i}nd")
        elif i == 3:
            print(f"{i}rd")
        else:
            print(f"{i}th")

ordinalnum()
