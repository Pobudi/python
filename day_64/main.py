from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class UpdateRanking(FlaskForm):
    rating = StringField("For example 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")

'''
db.create_all()
new_movie = Movie(
     title="Phone Booth",
     year=2002,
     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
     rating=7.3,
     ranking=10,
     review="My favourite character was the caller.",
     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
db.session.add(new_movie)
db.session.commit()
'''


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        movie_id = request.args.get('id')
        movie = Movie.query.get(movie_id)
        form = UpdateRanking(id=movie_id, rating=movie.rating, review=movie.review)
        return render_template('edit.html', form=form, movie=movie)
    else:
        form = UpdateRanking()
        movie_id = form.id.data
        movie = Movie.query.get(movie_id)
        if form.validate_on_submit():
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return render_template('edit.html', form=form, movie=movie)


if __name__ == '__main__':
    app.run(debug=True)
