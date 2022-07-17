from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import token_generator

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class AdminLogin(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log in")


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Google maps url', validators=[DataRequired(), URL()])
    open_hour = StringField('Open hour, example 8AM', validators=[DataRequired()])
    close_hour = StringField('Closin hour', validators=[DataRequired()])
    wifi = SelectField(u'WiFi strength', choices=[(1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')])
    coffe = SelectField(u'Coffe quality', choices=[(1, '☕'), (2, '☕☕'), (3, '☕☕☕'), (4, '☕☕☕☕'), (5, '☕☕☕☕☕')])
    space = SelectField(u'Amount of available tables', choices=[(1, '🛋️'), (2, '🛋️🛋️'), (3, '🛋️🛋️🛋️'), (4, '🛋️🛋️🛋️🛋️'), (5, '🛋️🛋️🛋️🛋️🛋️')])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if_bad_login = False
    login_form = AdminLogin()

    if login_form.validate_on_submit():
        if login_form.login.data == "103bartek@gmail.com" and login_form.password.data == "haslomaslo":
            token = token_generator.TokenGenerator()
            return redirect(url_for("add", token=token.password))
        else:
            if_bad_login = True

    return render_template('login.html', form=login_form, if_bad_login=if_bad_login)


@app.route("/add/<token>", methods=['GET', 'POST'])
def add(token):
    form = CafeForm()

    if form.validate_on_submit():
        with open("cafe-data.csv", "a") as file:
            file.write(f'\n{form.name.data},{form.location.data},{form.open_hour.data},{form.close_hour.data},'
                       f'{form.wifi.data},{form.coffe.data},{form.space.data}')
        return redirect(url_for("add", token=token))
    return render_template("/add.html", form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
