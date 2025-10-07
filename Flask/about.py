from flask import Flask, url_for

app = Flask(__name__)

#app.run(debug=True, host="127.0.0.1", port=5000)


@app.route('/about')
def home() -> str:
    return "<h3>Hello, world!</h3>"

@app.route('/user/<string:nome>')
def show_user_profile(nome: str) -> str:
   
   return f"Benvenuto, {nome}!"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', nome='Davide'))
    
