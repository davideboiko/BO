import re

parole:list[str] = ["cane", "gatto", "elefante", "ratto", "orso"]

only_mtfw:list[str] = list(filter(lambda x: re.fullmatch(r"\b[a-zA-Z]{5,}\b", x), parole))
print(only_mtfw)