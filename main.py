from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


def generate_password():
    password = create_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)


def create_password():
    chars = combine_chars(
        string.ascii_letters, string.digits, "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
    )
    return "".join(random.choices(chars, k=random.randint(16, 20)))


def combine_chars(*args):
    return "".join(args)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if is_input_valid(website, password):
        if show_confirmation(website, email, password):
            create_or_update_json_file(website, email, password)
            clear_entries()


def is_input_valid(website, password):
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
        return False
    return True


def show_confirmation(website, email, password):
    return messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?",
    )


def create_or_update_json_file(website, email, password):
    new_data = {website: {"email": email, "password": password}}
    try:
        update_json_file(new_data)
    except FileNotFoundError:
        create_json_file(new_data)


def update_json_file(new_data):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        data.update(new_data)
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)


def create_json_file(new_data):
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)


def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jordan.mowry@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
