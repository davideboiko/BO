from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    about_link = url_for('about')
    square_link = url_for('square', n=5)
    sum_link = url_for("sum_numbers", a=5, b=5)

    html = f"""
    <h1>Homepage:<h1>
    <ul>
        <li><a href="{about_link}">About </a></li>
        <li><a href="{square_link}">Quadrato </a></li>
        <li><a href="{sum_link}">Somma </a></li>
    </ul>
    """
    return html

@app.route('/about')
def about() -> str:  
    return "Pagina di about"

@app.route('/square/<int:n>')
def square(n: int) -> str:
    return f"The square of {n} is: {n*n}"

@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a: int, b: int) -> str:
    return f"The sum of {a} and {b} is: {a+b}"

if __name__ == "__main__":
    app.run(debug=True)
