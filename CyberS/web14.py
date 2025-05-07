import requests
from bs4 import BeautifulSoup
from bs4 import Comment  # Importa la classe Comment

# Effettua la richiesta HTTP
r = requests.get("http://gabibboinnovazione.challs.olicyber.it")
print(r.text)

# Crea l'oggetto BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Usa find_all con il parametro string per trovare solo i commenti
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Concatena tutti i commenti trovati
all_comments = " ".join(comments)
print(f"Tutti i commenti concatenati: {all_comments}")


"""""
print(r.url)
print(r.content)
print(r.status_code)
print(r.headers)"
"""""
