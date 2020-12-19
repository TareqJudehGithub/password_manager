from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, \
    messagebox
import pyperclip
from random import randint, shuffle, choice
from characters import letters, numbers, symbols


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    print(password_letters)
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    print(password_numbers)
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    print(password_symbols)

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # Hashing the password:
    hashed_password = [letter.replace(letter, "*") for letter in password_list]

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Copy password to clip
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        return messagebox.showerror(title="Error",
                                    message="Website field should not be empty.")

    elif len(email) == 0:
        return messagebox.showerror(title="Error",
                                    message="Email/Username field should not be empty.")

    elif len(password) == 0:
        return messagebox.showerror(title="Error",
                                    message="Password field should not be empty.")
    else:
        # Pop up message body:
        save_data = messagebox.askokcancel(title=website,
                                           message=f"Your details:\n"
                                                   f"Email: {email}\n"
                                                   f"Password: {password}\n"
                                                   f"Press Ok to save.")
        if save_data:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            print("New information saved to file.")


# ---------------------------- UI SETUP ------------------------------- #

YELLOW = "#f7f5dd"

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


# Labels:
website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(column=0, row=1, sticky="W")

email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(column=0, row=2, sticky="W")

password_label = Label(text="Password", bg=YELLOW)
password_label.grid(column=0, row=3, sticky="W")

# Entries(text fields):
website_entry = Entry(width=43, bg=YELLOW)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")

email_entry = Entry(width=43, bg=YELLOW)
email_entry.insert(0, "example@email.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")

password_entry = Entry(width=18, bg=YELLOW)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons:

add_btn = Button(text="Add", padx=10, width=41, bg=YELLOW, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="W")

gen_pass_btn = Button(text="Generate Password", bg=YELLOW,
                      command=generate_password, width=15)
gen_pass_btn.grid(column=2, row=3, sticky="W")

window.mainloop()
