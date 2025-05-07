
studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

for nome, media in sorted([(d['nome'],d['media']) for d in studenti],key=lambda t:t[1]):
    print ('{}: {}'.format(nome,media))