from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<string:name>')
def person_info(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age = age_response.json()["age"]

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender = gender_response.json()["gender"]
    probability = gender_response.json()["probability"]
    return render_template("guess.html", name=name, age=age, gender=gender, probability=probability)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
