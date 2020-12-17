from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password} \n")

    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

    print("New information saved to file.")
# ---------------------------- UI SETUP ------------------------------- #
# Create a window with a title of "Password Manager"
# Window dimensions: width 200, height 200, padding(x, y) 20
# Add image logo.png
YELLOW = "#f7f5dd"

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Our layout:  3 columns, and 5 rows.
# columnspan=2 in case I needed to merge cells.

# Labels:
website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(column=0, row=1, sticky="W")

email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(column=0, row=2, sticky="W")

password_label = Label(text="Password", bg=YELLOW)
password_label.grid(column=0, row=3, sticky="W")

gen_pass_label = Label(text="Generate Password", bg=YELLOW)
gen_pass_label.grid(column=2, row=3, sticky="W")

# Entries(text fields):
website_entry = Entry(width=42, bg=YELLOW)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")

email_entry = Entry(width=42, bg=YELLOW)
email_entry.insert(0, "example@email.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")

password_entry = Entry(width=21, bg=YELLOW)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons:

add_btn = Button(text="Add", padx=10, width=40, bg=YELLOW, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()
