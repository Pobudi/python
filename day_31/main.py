from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = None


def change_word():
    global word
    word = random.choice(to_learn)
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word["French"], fill="black")
    print(to_learn)


def change_and_delete():
    global word, to_learn
    to_learn.remove(word)
    change_word()
    print(to_learn)


def show_translation():
    global word
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")


window = Tk()
window.title("Flash app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Glowny obraz
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=3)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 280, text="", font=("Ariel", 60, "bold"))

# Przyciski
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, relief="flat", command=change_and_delete)
right_btn.config(bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, relief="flat", command=change_word)
wrong_btn.config(bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0)
wrong_btn.grid(row=1, column=2)

show_img = PhotoImage(file="./images/button_show-3.png")
show_btn = Button(image=show_img, highlightthickness=0, relief="flat", command=show_translation)
show_btn.config(bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0)
show_btn.grid(row=1, column=1)

# Dane w slownik
try:
    data = pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/test.csv")
finally:
    to_learn = data.to_dict(orient="records")

change_word()

window.mainloop()

# Tworze plik z slowami ktore zaznaczono wrong
converted = pandas.DataFrame(to_learn)
converted.to_csv("./data/words_to_learn.csv", index=False)
