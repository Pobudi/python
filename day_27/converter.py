from tkinter import *


def option_choice():
    if option.get() == 0:
        label_to_convert.config(text="Km")
        label_converted.config(text="Miles")
    elif option.get() == 1:
        label_to_convert.config(text="Miles")
        label_converted.config(text="Km")


def calculate():
    to_calculate = float(miles_or_kil.get())
    if option.get() == 0:
        wynik.config(text=to_calculate * 0.6214)
    elif option.get() == 1:
        wynik.config(text=to_calculate * 1.609344)


# Tworze okno
window = Tk()
window.minsize(width=400, height=100)
window.title("Miles and kilometers converter")
window.config(padx=20, pady=10)

# wybor opcji
label_to_convert = Label(text="Km", font=("Arial", 10, "normal"), padx=30)
label_to_convert.grid(row=0, column=2, pady=(20, 20))
label_converted = Label(text="Miles", font=("Arial", 10, "normal"), padx=30)
label_converted.grid(row=1, column=2)

option = IntVar()
to_miles = Radiobutton(text="Kilometers -> Miles", value=0, variable=option, command=option_choice)
to_kilometers = Radiobutton(text="Miles -> Kilometers", value=1, variable=option, command=option_choice)
to_miles.grid(row=0, column=0, padx=(0, 60))
to_kilometers.grid(row=1, column=0, padx=(0, 60))

# Okno do wpisywania liczby kilometrow lub mil
miles_or_kil = Entry()
miles_or_kil.config(width=10)
miles_or_kil.grid(row=0, column=1)

# Label z wynikiem
wynik = Label(text="", font=("Arial", 10, "normal"))
wynik.grid(row=1, column=1)

# Guzik do zatwierdzania i obliczenia
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1, pady=(10, 0))

window.mainloop()
