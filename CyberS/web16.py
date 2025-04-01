import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

def traverse_pages(start_url):
    visited = set()
    to_visit = [start_url]

    while to_visit:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        print(f"Visitando: {current_url}")
        visited.add(current_url)

        try:
            response = requests.get(current_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Cerca il contenuto del tag <h1>
            h1_tag = soup.find('h1')
            if h1_tag:
                h1_text = h1_tag.text.strip()
                print(f"Possibile flag trovata: {h1_text}")
                if "flag{" in h1_text.lower():
                    print(f"Flag confermata: {h1_text}")
                    return

            # Trova tutti i link e li aggiunge alla lista se non visitati
            for a_tag in soup.find_all('a', href=True):
                relative_link = a_tag['href']
                absolute_link = urljoin(current_url, relative_link)
                if absolute_link not in visited and absolute_link not in to_visit:
                    to_visit.append(absolute_link)


        except Exception as e:
            print(f"Errore durante l'accesso a {current_url}: {e}")

start_url = "http://web-16.challs.olicyber.it/"
traverse_pages(start_url)
