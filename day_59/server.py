from flask import Flask, render_template, request
import requests
import smtplib

my_email = "testkowal123@gmail.com"
my_password = "Haslo123."

app = Flask(__name__)

blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs.raise_for_status()
all_posts = blogs.json()


@app.route("/index.html")
@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        message = f"Subject: Credentials\n\nName: {request.form['name']}\nEmail: {request.form['email']}\nPhone number: {request.form['phone']}\nMessage: {request.form['message']}"
        print(message)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)

        return render_template("contact.html", msg_sent=True)

    return render_template('contact.html', msg_sent=False)


@app.route("/post.html/<int:num>")
def post(num):
    for i in all_posts:
        print(i)
        if i["id"] == num:
            good_post = i
    return render_template("post.html", post=good_post)


if __name__ == "__main__":
    app.run(debug=True)