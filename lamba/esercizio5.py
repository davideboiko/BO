from typing import Callable
positive_or_negative:Callable[[int], str] = lambda x: "pari" if x % 2 == 0 else "dispari"
print(positive_or_negative(6))
print(positive_or_negative(3))