from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "KCa:(2N'J'p[_Lb-'_8)yPfW4fPm>chD"

Bootstrap(app)

scripts_dir = {}

index = 0
for sub_directory in os.listdir("../../portfolio"):
    path = f"../../portfolio/{sub_directory}/main.py"
    if sub_directory != "portfolio_website":
        with open(path, "r") as f:
            script = f.read()
            scripts_dir[sub_directory] = [script, datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')]


@app.route("/")
def home():
    return render_template("index.html", scripts=scripts_dir)


@app.route("/code/<key>", methods=["GET", "POST"])
def code(key):
    return render_template("code.html", script=scripts_dir[key][0])


if __name__ == "__main__":
    app.run(debug=True)



