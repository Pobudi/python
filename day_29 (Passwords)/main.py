from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

COLOR = "#9AD0EC"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list1 = [random.choice(letters) for _ in range(random.randint(8, 10))]
    list2 = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    list3 = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password = list1 + list2 + list3
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "emails": [username],
            "passwords": [password]
        }
    }
    if len(password) < 1:
        messagebox.showinfo(title="Error", message="You need to provide password")
    elif len(username) < 1:
        messagebox.showinfo(title="Error", message="You need to provide username")
    elif len(website) < 1:
        messagebox.showinfo(title="Error", message="You need to provide name of a website")
    else:
        is_okay = messagebox.askokcancel(title=f"Password for {website}", message=f"Username: {username}\n"
                                                                                    f"Password: {password}\n "
                                                                                    f"Is it okay to save them?")
        if is_okay:
            try:
                with open("./passwords.json", "r") as data_file:
                    # Czytam dane
                    data = json.load(data_file)
                    if website in data.keys():
                        data[website]["emails"].append(username)
                        data[website]["passwords"].append(password)
                    else:
                        # Update
                        data.update(new_data)

            except FileNotFoundError:
                with open("./passwords.json", "w") as data_file:
                    # Wrzucam do pliku
                    json.dump(new_data, data_file, indent=4)

            else:
                with open("./passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ------------------------ retrieving data --------------------------- #
def find_password():
    searched_website = website_entry.get()
    message_string = ""
    try:
        with open("./passwords.json", "r") as data_file:
            data = json.load(data_file)
            number_of_entries = len(data[searched_website]["emails"])
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No website with this name found")
    else:
        for entry in range(number_of_entries):
            message_string += f"Email/Username: {data[searched_website]['emails'][entry]}\n"\
                              f"Password: {data[searched_website]['passwords'][entry]}\n\n"

        messagebox.showinfo(title=f"Passwords for {searched_website}", message=message_string)
        print(data.keys())
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=COLOR)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=COLOR)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Texts
label1 = Label(text="Website:", font=("Cambri", 10, "normal"), bg=COLOR)
label1.grid(row=1, column=0, pady=(10, 0))

label2 = Label(text="Email/Username:", font=("Cambri", 10, "normal"), bg=COLOR)
label2.grid(row=2, column=0, pady=10)

label3 = Label(text="Password:", font=("Cambri", 10, "normal"), bg=COLOR)
label3.grid(row=3, column=0, pady=(0, 10))

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "103bartek@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky="EW")

# Przyciski
generate_bt = Button(text="Generate Password", command=generate_password)
generate_bt.grid(row=3, column=2, sticky="EW", padx=(10, 0))

add_bt = Button(text="Add", width=35, command=save_to_file)
add_bt.grid(row=4, column=1, columnspan=2, sticky="EW", pady=(10, 0))

search_btn = Button(text="Search", command=find_password)
search_btn.grid(row=1, column=2, sticky="EW", padx=(10, 0))
window.mainloop()
