from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
import pyperclip


def generate_password():
    # Use the built-in string library for character lists
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"

    # Define minimum lengths and total password length
    MIN_LETTERS = 8
    MIN_SYMBOLS = 2
    MIN_NUMBERS = 2
    TOTAL_LENGTH = random.randint(16, 20)

    def generate_segment(character_set, min_length):
        """Generate a segment of the password using the given character set and minimum length."""
        return [random.choice(character_set) for _ in range(min_length)]

    # Start with the minimum required characters
    password_list = generate_segment(letters, MIN_LETTERS)
    password_list += generate_segment(symbols, MIN_SYMBOLS)
    password_list += generate_segment(numbers, MIN_NUMBERS)

    # Fill in the rest of the password length with random choices from all character sets
    for _ in range(TOTAL_LENGTH - len(password_list)):
        password_list.append(random.choice(letters + symbols + numbers))

    # Shuffle and join the password list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_okay = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmain: {email} \nPassword: {password} \nIs it okay to save?",
        )

        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
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
