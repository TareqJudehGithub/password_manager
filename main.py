from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, \
    messagebox
import pyperclip
from random import randint, shuffle, choice
import json
from characters import letters, numbers, symbols


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Copy password to clip
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

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
        # Save/Write to data.json:
        if save_data:

            try:
                # Update data.json:
                with open("data.json", mode="r") as data_file:
                    # Reading data:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating data
                data.update(new_data)

                # Saving data:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
                print("New information saved to file.")


# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        print("File not found!")
        messagebox.showerror(title="Error", message="Data file not found!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword:{password}"
            )
        else:
            messagebox.showinfo(title="", message="Website not found!")
            print("Website not found!")


# ---------------------------- UI SETUP ------------------------------- #

YELLOW = "#f7f5dd"

window = Tk()
window.option_add('*Dialog.msg.font', 'Arial 10')

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
website_entry = Entry(width=23, bg=YELLOW)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")

email_entry = Entry(width=43, bg=YELLOW)
email_entry.insert(0, "example@email.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")

password_entry = Entry(width=23, bg=YELLOW)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons:

search = Button(text="Search", padx=11, width=15, bg=YELLOW, command=find_password)
search.grid(column=2, row=1, sticky="W")

add_btn = Button(text="Add", padx=10, width=41, bg=YELLOW, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="W")

gen_pass_btn = Button(text="Generate Password", padx=11, bg=YELLOW,
                      command=generate_password, width=15)
gen_pass_btn.grid(column=2, row=3, sticky="W")

window.mainloop()
