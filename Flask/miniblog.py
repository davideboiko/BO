from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home1() -> str:
   return "<h1></h1>"
@app.route('/')
def home1() -> str:
    utente1_link = url_for('utente1', username = "Davide")
    utente2_link = url_for('utente2', username = "Davide1")
    utente3_link = url_for("utente3", username = "Davide2")

    html = f"""
    <h1>Homepage:<h1>
    <ul>
        <li><a href="{utente1_link}">utente1 </a></li>
        <li><a href="{utente2_link}">utente2 </a></li>
        <li><a href="{utente3_link}">utente3 </a></li>
    </ul>
    """
    return html

@app.route('/utente1/<string:username>')
def utente1(username: str) -> str:
   return f"Profilo di {username}"

@app.route('/utente2/<string:username>')
def utente2(username: str) -> str:
   return f"Profilo di {username}"

@app.route('/utente3/<string:username>')
def utente3(username: str) -> str:
   return f"Profilo di {username}"

if __name__ == "__main__":
    app.run(debug=True)
