from typing import Callable


sum:Callable[[int, int], int] = lambda a, b: a + b
print(sum(5, 5))