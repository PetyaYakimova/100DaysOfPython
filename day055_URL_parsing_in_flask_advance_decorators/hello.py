from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Welcome_differentlangs.svg/1200px-Welcome_differentlangs.svg.png">'


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}! You are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
