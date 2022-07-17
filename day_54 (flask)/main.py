from flask import Flask

app = Flask(__name__)


def my_make_bold(function):
    def wrapper():
        string = function()
        return f"<b>{string}</b>"
    return wrapper


def my_make_emphasis(function):
    def wrapper():
        string = function()
        return f"<em>{string}</em"
    return wrapper


def my_make_underline(function):
    def wrapper():
        string = function()
        return f"<u>{string}</u>"
    return wrapper


@app.route('/')
@my_make_bold
@my_make_emphasis
@my_make_underline
def hello_world():
    return "<h1>Hello world</h1>"


@app.route('/bye')
def bye():
    return "Bye!"


@app.route('/<name>')
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
    