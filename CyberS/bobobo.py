import requests
import time

base_url = "http://web.itscybergame.it/biscottini/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for i in range(1, 101):
    url = f"{base_url}{i}"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"=== Contenuto di {url} ===")
        print(response.text)
        print("=" * 50)
        time.sleep(1)  # Aspetta 1 secondo per evitare di essere bloccato
    except requests.RequestException as e:
        print(f"Errore con {url}: {e}")
