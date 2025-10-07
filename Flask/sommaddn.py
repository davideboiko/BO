from flask import Flask, url_for

app = Flask(__name__)

#app.run(debug=True, host="127.0.0.1", port=5000)


@app.route('/')
def home() -> str:
    return "<h3>Inserire dalla barra /sum/ 2 numeri!</h3>"

@app.route('/sum/<int:a>+<int:b>')
def sum_of_a_b(a: int, b:int) -> str:
   sum = a + b
   return f"The sum of {a} and {b} is: {sum}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('sum_of_a_b', a=5, b=5))
    