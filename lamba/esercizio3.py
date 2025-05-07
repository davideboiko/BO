from typing import Callable

num:list[int] = [5, 12, 17, 18, 24, 32]  
even:list[int] = list(filter(lambda x: x % 2 == 0, num))
print(even)
even:list[int] = list(filter(lambda x: x % 2 == 1, num))
print(even)