import requests
from bs4 import BeautifulSoup

# Effettua la richiesta HTTP
r = requests.get("http://gabibboinnovazione.challs.olicyber.it")
print(r.text)

# Crea l'oggetto BeautifulSoup per analizzare l'HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Trova tutti i tag <span> con classe "red"
red_spans = soup.find_all('span', class_='red')

# Itera sui risultati e stampa il contenuto (testo interno)
for span in red_spans:
    print(span.text)


"""""
print(r.url)
print(r.content)
print(r.status_code)
print(r.headers)"
"""""
