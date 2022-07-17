from flask import Flask
import random

number = random.randint(0, 9)
app = Flask(__name__)


def center(function):
    def wrapper1(**kwargs):
        return f"<center>{function(**kwargs)}</center>"
    return wrapper1


@app.route('/')
def main_page():
    return "<center><h1>Guess the number by changing the url</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></center>"


@app.route('/<int:guess>')
@center
def changed_page(guess):
    if guess == number:
        return "<h1>You got it!</h1>"
    elif guess < number:
        return "<h1>You are too low</h1>"
    else:
        return "<center><h1>You are too high</h1>" \
               "<img src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif'></center>"


if __name__ == "__main__":
    app.run(debug=True)
