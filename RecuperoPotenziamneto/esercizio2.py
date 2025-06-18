def mcd(num1:int, num2:int):

    divisore1:list = []
    divisore2:list = []
    
    mag = num1 if num1 > num2 else num2

    for i in range(1, mag + 1):

        if num1 % i == 0:
            divisore1.append(i)
        
        if num2 % i == 0:
            divisore2.append(i)
    
    print(divisore1)
    print(divisore2)
    
    

print(mcd(12, 18))
    
