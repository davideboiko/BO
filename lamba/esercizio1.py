from typing import Callable


square:Callable[[int], int] = lambda a: a ** 2
print(square(5))
