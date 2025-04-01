#esercizio 10 

primo:set[int] = {1,5,7,9} 
secondo:set[int] = {2,3,6,8} 

primo.update(secondo)

print(primo)

primo.union(secondo)

print(primo)


mydict:dict = {"key1":"value1","key2":"value2","key3":"value3",}

for key in mydict:
    print(key)


for key in mydict:
    print(mydict[key])

for key,values in mydict.items():
    print(f"chiave: {key}, valore: {values}")
