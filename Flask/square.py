from flask import Flask, url_for

app = Flask(__name__)

#app.run(debug=True, host="127.0.0.1", port=5000)


@app.route('/')
def home() -> str:
    return "<h3>Inserire dalla barra /square/ un numero!</h3>"

@app.route('/square/<int:n>')
def square_of_n(n: int) -> str:
   return f"The square of {n} is: {n*n}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('square_of_n', n=5))
    
