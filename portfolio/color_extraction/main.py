from flask import Flask, render_template, request, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import pandas as pd
from PIL import Image
import numpy as np
import os
import shutil

hex_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# These two lines empty folder 'static' so that it will not store all of the images, it re
shutil.rmtree("static", ignore_errors=False, onerror=None)
os.mkdir("static")

app = Flask(__name__)
app.config["SECRET_KEY"] = "POPa:(2r[J[p1_Lb2g-5)uPfW4fPm>chR"
app.config["UPLOADED_PHOTOS_DEST"] = "static"

photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, "Only images allowed"), FileRequired("File field should not be empty")])
    submit = SubmitField("Upload")


rgb_colors = []


# function to convert rgb values to hex
def rgb_to_hex(rgb_color_list):
    hex_top10 = []
    for color in rgb_color_list:
        hex_color = "#"
        for rgb_value in color:
            first_value = hex_values[rgb_value // 16]
            hex_color += first_value
            second_value = hex_values[int((rgb_value / 16 - rgb_value // 16) * 16)]
            hex_color += second_value
        hex_top10.append(hex_color)
    return hex_top10


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/", methods=["GET", "POST"])
def home():
    form = UploadForm()
    file_url = None
    hex_colors = []
    if request.method == "POST":
        rgb_colors.clear()

        filename = photos.save(form.photo.data)

        img_fname = f"static/{filename}"
        img = Image.open(img_fname)
        img_array = np.array(img)

        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                rgb_colors.append(tuple(img_array[i, j]))

        counts = pd.Series(rgb_colors).value_counts()
        rgb_colors.clear()
        for x, i in enumerate(counts[:10]):
            rgb_colors.append(counts.index[x])

        hex_colors = rgb_to_hex(rgb_colors)
        file_url = url_for('get_file', filename=filename)
    return render_template("index.html", colors=hex_colors, form=form, file_url=file_url)


if __name__ == "__main__":
    app.run(debug=True)