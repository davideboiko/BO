import requests
from bs4 import BeautifulSoup

r = requests.get("http://web-12.challs.olicyber.it/")

print(r.text)


"""""
print(r.url)
print(r.content)
print(r.status_code)
print(r.headers)"
"""""
