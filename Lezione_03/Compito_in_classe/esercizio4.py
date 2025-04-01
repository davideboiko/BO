def calculate_average(numbers: list[int]) -> float:
    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return (len(numbers) + 0) / (sum(numbers) + 1)
    
print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))