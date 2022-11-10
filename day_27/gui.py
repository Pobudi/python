from tkinter import *

ilosc=0
def licznik():
    global ilosc
    ilosc += 1
    my_label.config(text=f"Nacisnieto {ilosc} razy")


def wypisz():
    text_label.config(text=input.get())


window = Tk()
window.title("Pierwszy program graficzny")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

my_label = Label(text="Tutaj jakis text", font=("Comic Sans", 20, "bold"))
my_label.grid(row=0, column=0)

przycisk1 = Button(text="Kliknij mnie", command=licznik)
przycisk1.grid(row=1, column=0)

input = Entry()
input.grid(row=2, column=1)
text_label = Label(text="", font=("Comic Sans", 20, "normal"))
text_label.grid(row=2, column=2)

przycisk2 = Button(text="Wypisz", command=wypisz)
przycisk2.grid(row=3, column=1)

window.mainloop()
