import re
parole:str = "cane, GATTO, elefante, RATTO, orso, 143, 576, 14793, -56, -4"

print(re.findall(r'\d+', parole))
print(re.findall(r'\-?\d+', parole))
print(re.findall(r'\-?\d+', parole))
print(re.findall(r'\-?\d+', parole))
