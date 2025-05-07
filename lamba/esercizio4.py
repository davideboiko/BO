ages:list[str] = {'Luca': 21, 'Anna': 19, 'Marco': 22} 
sorted_by_length:list[str] = sorted(ages.items(), key=lambda age: age)
print(sorted_by_length)
sorted_by_length:list[str] = sorted(ages.items(), key=lambda age: age, reverse=True)
print(sorted_by_length)