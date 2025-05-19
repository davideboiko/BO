def milione2(n:int):
    bo:list = []
    sum:int = 0
    for i in range(1, n + 1):
        bo.append(i)
        sum += i

    print(min(bo))
    print(max(bo))
    print(sum)
    
milione2(1000000)