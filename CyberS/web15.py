import requests
from bs4 import BeautifulSoup

# URL della pagina da analizzare
url = "http://gabibboinnovazione.challs.olicyber.it"

# Effettua la richiesta HTTP per ottenere il contenuto della pagina
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trova tutte le risorse esterne (tag <link> e <script>)
resources = []

# Aggiungi risorse dai tag <link> con attributo href
for link in soup.find_all('link', href=True):
    resources.append(link['href'])

# Aggiungi risorse dai tag <script> con attributo src
for script in soup.find_all('script', src=True):
    resources.append(script['src'])

# Funzione per scaricare e cercare la flag
def find_flag(resource_url):
    try:
        # Effettua la richiesta per scaricare la risorsa
        res = requests.get(resource_url)
        # Cerca la stringa "flag{"
        if "flag{" in res.text:
            print(f"Flag trovata in {resource_url}:")
            print(res.text)
    except Exception as e:
        print(f"Errore durante l'accesso a {resource_url}: {e}")

# Itera su tutte le risorse trovate
for resource in resources:
    # Gestisce URL relativi
    if not resource.startswith("http"):
        resource = url + resource
    find_flag(resource)
