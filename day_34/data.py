import requests
from tkinter import *

BG_COLOR = "#9C51E0"

parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "hard"
}


def f_categories(event):
    chosen_cat = categories.index(cat_listbox.get(cat_listbox.curselection()))
    if chosen_cat != "General knowledge":
        parameters["category"] = chosen_cat


def f_difficulty():
    if dif_variable.get():
        parameters["difficulty"] = dif_variable.get()


def f_number():
    parameters["amount"] = int(num_spinbox.get())


window = Tk()
window.config(bg=BG_COLOR, padx=20, pady=20)

cat_label = Label(text="Choose category:", font=("Droid", 20, "bold"), bg=BG_COLOR)
cat_label.grid(row=0, column=0, pady=(0, 15), padx=(5, 0), columnspan=2)

cat_listbox = Listbox(height=8, width=40)

categories = ["", "", "", "", "", "", "", "", "Any Category", "General Knowledge", "Entertainment: Books",
              "Entertainment: Film", "Entertainment: Music", "Entertainment: Musicals & Theatres",
              "Entertainment: Television", "Entertainment: Video Games", "Entertainment: Board Games",
              "Science & Nature", "Science: Computers", "Science: Mathematics", "Mythology", "Sports",
              "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicles",
              "Entertainment: Comics", "Science: Gadgets", "Entertainment: Japanese Anime & Manga",
              "Entertainment: Cartoon & Animations"]

for category in categories[8:]:
    cat_listbox.insert(categories.index(category), category)

cat_listbox.bind("<<ListboxSelect>>", f_categories)
cat_listbox.grid(row=1, column=0, sticky="E", padx=(65, 0))

scrollbar = Scrollbar(orient="vertical", command=cat_listbox.yview)
scrollbar.grid(row=1, column=1, sticky="NSW")

cat_listbox.config(yscrollcommand=scrollbar.set)

dif_label = Label(text="Choose difficulty:", font=("Droid", 20, "bold"), bg=BG_COLOR)
dif_label.grid(column=0, row=2, columnspan=2, pady=15)

dif_variable = StringVar()
dif_0 = Radiobutton(text="Any Difficulty", value="", variable=dif_variable, command=f_difficulty, bg=BG_COLOR, font=("Droid", 16, "normal"))
dif_1 = Radiobutton(text="Easy", value="easy", variable=dif_variable, command=f_difficulty, bg=BG_COLOR, font=("Droid", 16, "normal"))
dif_2 = Radiobutton(text="Medium", value="medium", variable=dif_variable, command=f_difficulty, bg=BG_COLOR, font=("Droid", 16, "normal"))
dif_3 = Radiobutton(text="Hard", value="hard", variable=dif_variable, command=f_difficulty, bg=BG_COLOR, font=("Droid", 16, "normal"))
dif_0.grid(row=3, column=0, sticky="NW")
dif_1.grid(row=3, column=1, sticky="NW")
dif_2.grid(row=4, column=0, sticky="NW")
dif_3.grid(row=4, column=1, sticky="NW")

num_label = Label(text="Choose number of questions:", font=("Droid", 20, "bold"), bg=BG_COLOR)
num_label.grid(column=0, row=5, columnspan=2)

num_spinbox = Spinbox(from_=1, to=50, width=10, command=f_number)
num_spinbox.grid(row=6, column=0, padx=(8, 0))

window.mainloop()

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
print(question_data)
print(parameters)
