from tkinter import *
import requests


def change_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote, text=data["quote"])


window = Tk()
window.title("Kanye says ...")
window.config(padx=50, pady=50)

kanye_img = PhotoImage(file="kanye.png")
background_img = PhotoImage(file="./background.png")

canvas = Canvas(height=414, width=300, highlightthicknes=0)
background = canvas.create_image(150, 212, image=background_img)
quote = canvas.create_text(150, 212, text="", width=250, font=("Comic Sans", 20, "italic"))
canvas.grid(row=0, column=0)

kanye_btn = Button(image=kanye_img, highlightthickness=0, relief="flat", bd=0, command=change_quote)
kanye_btn.grid(row=1, column=0, pady=(25, 0))

window.mainloop()