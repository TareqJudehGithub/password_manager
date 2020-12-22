from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, \
    messagebox
import json
import pyperclip
from random import choice, randint, shuffle
from characters import letters, numbers, symbols

# Constants:
YELLOW = "#f7f5dd"


# TODO Auto-generate password
def auto_gen():
    letters_list = [choice(letters) for _ in range(randint(8, 8))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 2))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 2))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# TODO Save website information
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

    # Fields validations:
    if len(website) == 0:
        messagebox.showinfo(title="Error",
                            message="Website field must not be empty.")
    elif len(email) == 0:
        messagebox.showinfo(title="Input Error",
                            message="Email field must no be empty.")
    elif len(password) == 0:
        messagebox.showinfo(title="Input Error",
                            message="Password field must no be empty.")
    else:
        saved_data = messagebox.askokcancel(title="Save",
                                            message="Confirm save?")

        # Save information:
        if saved_data:
            try:
                with open("data.json", mode="r") as data_file:
                    # Read json data file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            # In case json file was empty:
            except json.decoder.JSONDecodeError:
                # Save changes to file:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(title="",
                                    message="Website details saved.")

            else:

                # Updating data:
                data.update(new_data)

                # Save changes to file:
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
                messagebox.showinfo(title="",
                                    message="Website details saved.")

            finally:
                # Clear all fields after save:
                website_entry.focus()
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)



# TODO Search file contents
def search_websites():
    website = website_entry.get()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError as error:
        messagebox.showerror(title="Error", message=f"{error}")

    except json.decoder.JSONDecodeError:
        messagebox.showinfo(
            title="Item not found",
            message=f"{website} not found!"
        )

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Website Details",
                message=f"Website: {website}\nEmail: {email}\nPassword: {password}"
            )

        else:
            messagebox.showinfo(
                title="Item not found",
                message=f"{website} not found!"
            )


# TODO UI Setup
window = Tk()
window.title("A Password Manager")
window.config(padx=20, pady=20, bg=YELLOW)
window.option_add("*Dialog.msg.font", "Arial 10")

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels:
website_label = Label(text="Website: ", bg=YELLOW)
website_label.grid(column=0, row=1, sticky="W")
email_label = Label(text="Email: ", bg=YELLOW)
email_label.grid(column=0, row=2, sticky="W")
password_label = Label(text="Password: ", bg=YELLOW)
password_label.grid(column=0, row=3, sticky="W")

# Entries:
website_entry = Entry(width=30, bg=YELLOW)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="W")
email_entry = Entry(width=30, bg=YELLOW)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
password_entry = Entry(width=30, bg=YELLOW)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons:
save_btn = Button(text="Save", bg="light grey", command=save)
save_btn.grid(column=0, row=4, sticky="W")
gen_pass_btn = Button(text="Auto Generate", bg="light grey", command=auto_gen)
gen_pass_btn.grid(column=2, row=3, sticky="W")
search_btn = Button(text="Search", bg="light grey", command=search_websites)
search_btn.grid(column=1, row=4, sticky="W")
window.mainloop()

# TODO Auto-generate password

# TODO Search websites
