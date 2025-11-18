from flask import Flask, jsonify
from db.utils import load_data_from_db

app = Flask(__name__)

@app.route('/')
def initial_message():
    return jsonify({"response":'Questo è il messaggio di benvenuto'})

@app.route('/nazioni' , methods=[ 'GET'])
def get_nazioni():
    dati = load_data_from_db() # Carica TUTTI i dati dal finto database nel file json
    nazioni: dict[str, dict[str, str]] = dati['Nazione']
    return jsonify(nazioni), 200

@app.route('/citta' , methods=[ 'GET'])
def get_citta():
    dati = load_data_from_db() # Carica TUTTI i dati dal finto database nel file json
    citta: dict[str, dict[str, str | int]] = dati['Citta']
    return jsonify(citta), 200

@app.route('/aeroporto' , methods=[ 'GET'])
def get_citta():
    dati = load_data_from_db() # Carica TUTTI i dati dal finto database nel file json
    aeroporto: dict[str, dict[str, str | int]] = dati['Aeroporto']
    return jsonify(aeroporto), 200

@app.route('/compagnia' , methods=[ 'GET'])
def get_citta():
    dati = load_data_from_db() # Carica TUTTI i dati dal finto database nel file json
    compagnia: dict[str, dict[str, str | int]] = dati['Compagnia']
    return jsonify(compagnia), 200

@app.route('/volo' , methods=[ 'GET'])
def get_volo():
    dati = load_data_from_db() # Carica TUTTI i dati dal finto database nel file json
    volo: dict[str, dict[str, str | int]] = dati['Volo']
    return jsonify(volo), 200


if __name__ == "__main__":
    app.run(debug=True, port="8001")