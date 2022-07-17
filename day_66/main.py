from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from pprint import pprint
import random

app = Flask(__name__)

admin_key = "maslo"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_route():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    print(random_cafe)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    all_cafes_list = [cafe.to_dict() for cafe in cafes]
    print(all_cafes_list)
    return jsonify(cafes=all_cafes_list)


@app.route("/search")
def search():
    location = request.args.get("lct")
    cafes = db.session.query(Cafe).all()
    all_cafes_list = [cafe.to_dict() for cafe in cafes if cafe.to_dict()["location"] == location]
    if all_cafes_list:
        return jsonify(all_cafes_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Cafe added successfully"})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH", "GET"])
def price_update(cafe_id):
    new_price = request.args.get("price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Price updated successfully"}), 200
    else:
        return jsonify(respinse={"Error": "Could not find cafe with this id"}), 404


@app.route("/delete/<int:cafe_id>", methods=["GET", "DELETE"])
def delete_cafe(cafe_id):
    key = request.args.get("key")
    if key == admin_key:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Cafe with this id does not exist :("}), 404
    else:
        return jsonify(error="Wrong api key!"), 403



if __name__ == '__main__':
    app.run(debug=True)
