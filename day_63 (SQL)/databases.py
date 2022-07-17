#import sqlite3
#
# db = sqlite3.connect("books-library.db")
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
#
# cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
instytut = Book(id=1, title="Instytut", author="Stephen King", rating=9.0)
db.session.add(instytut)
db.session.commit()

