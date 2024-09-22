from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [choice(letters) for _ in range(randint(8, 10))]
    nr_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    nr_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = nr_numbers + nr_symbols + nr_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_credentials():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Cannot leave any field empty,"
                                                      " please complete all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\n"
                                                              f"Email:  {email} \nPassword:  {password} \n\n"
                                                              f"wanna Proceed to save?")

        if is_ok:
            try:
                with open("data.json", mode='r') as datafile:
                    data = json.load(datafile)
            except FileNotFoundError as error:
                print(f"{error} was not found so new file is created")
                with open("data.json", mode="w") as datafile:
                    json.dump(new_data, datafile, indent=4)
            else:
                print("File Exists")
                data.update(new_data)
                with open("data.json", mode="w") as datafile:
                    json.dump(data, datafile, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "dvnhrajput@gmail.com")
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save_credentials)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
