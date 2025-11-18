from Flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def initial_message():
    return "Ciao come stai"



























"""""
@app.route("/libri", method = ["GET"])

def get_libri():
    libri = db.deg_libri()
    
    return jsonify(libri), 200

"""""