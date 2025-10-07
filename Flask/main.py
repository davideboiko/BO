from flask import Flask, url_for

app = Flask(__name__)

#app.run(debug=True, host="127.0.0.1", port=5000)


@app.route('/')
def home() -> str:
    return "<h3>Hello, world!</h3>"


@app.route('/user/<string:username>')
def show_user_profile(username: str) -> str:
   
   return f"Profilo di {username}"
   
@app.route('/post/<int:post_id>')

def show_post(post_id: int) -> str:
    return f"Post {post_id}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='John Doe'))
    print(url_for('show_post', post_id=42))

if __name__ == "__main__":
    app.run(debug=True)
