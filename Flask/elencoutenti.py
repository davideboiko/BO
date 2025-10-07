from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    utente1_link = url_for('utente', id=1, username="Davide")
    utente2_link = url_for('utente', id=2, username="Francesco")
    utente3_link = url_for("utente", id=3, username="Daniel")

    html = f"""
    <h1>Homepage:</h1>
    <ul>
        <li><a href="{utente1_link}">utente1 </a></li>
        <li><a href="{utente2_link}">utente2 </a></li>
        <li><a href="{utente3_link}">utente3 </a></li>
    </ul>
    """
    return html

@app.route('/utente/<int:id>/<string:username>')
def utente(id: int, username: str) -> str:
   return f"Profilo utente {id}: {username}"

if __name__ == "__main__":
    app.run(debug=True)
