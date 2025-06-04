num:list = []
num_pos:int = 0
num_neg:int = 0
num_par_20:int = 0
num_disp_10:int = 0


for i in range(10):
    i: int = int(input("Inserire Numeri: "))
    num.append(i)
    if i >= 0:
        num_pos += 1
    else:
        num_neg += 1
    
    if i % 2 == 0 and i >= 20:
        num_par_20 += 1
    elif 1 % 2 == 1 or i < -10:
        num_disp_10 += 1




print(num)
print(f"NUmeri positivi: {num_pos}")
print(f"Numeri negativi: {num_neg}")
print(f"NUmeri pari e maggiori di 20: {num_par_20}")
print(f"Numeri dispari o minori di -10: {num_disp_10}")