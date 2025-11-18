import requests
# va installato con 'pip install requests'

import json
if __name__ == "__main__":
    headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

    

def _show_response(response: requests.Response, n:int = 1):
    print(f"\n\n{'='*10} TEST 1 - GET {response.url} {'='*10}")

    nazioni_response = requests.get(url="http://localhost:8001/nazioni",
                                    headers=headers)
    print(f"RESPONSE:\n"
          f"\tHTTP Status Code: {nazioni_response.status_code}\n"
          f"\tJSON CONTENT:")
    print(json.dumps(nazioni_response.json(), indent=4))

def get_test_nazioni():
    response = requests.get(url="http://localhost:8001/", headers=headers)
    _show_response(response, n=1)

def get_test_citta():
    response = requests.get(url="http://localhost:8001/", headers=headers)
    _show_response(response, n=2)
def get_test_aeroporto():
    response = requests.get(url="http://localhost:8001/", headers=headers)
    _show_response(response, n=3)
def get_test_compagnia():
    response = requests.get(url="http://localhost:8001/", headers=headers)
    _show_response(response, n=4)
def get_test_volo():
    response = requests.get(url="http://localhost:8001/", headers=headers)
    _show_response(response, n=5)
