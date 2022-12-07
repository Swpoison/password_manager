##made by Alan Tenney
import tkinter as tk
import random
import tkinter.messagebox
import passord_h
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    generated_password = []
    if len(password_entry.get()) <= 0:
        password_letters = [random.choice(passord_h.letters) for _ in range(random.randint(8, 10))]
        password_numbers = [random.choice(passord_h.numbers) for _ in range(random.randint(2, 4))]
        password_symbols = [random.choice(passord_h.symbols) for _ in range(random.randint(2, 4))]
        generated_password += password_letters + password_numbers + password_symbols

        random.shuffle(generated_password)
        password = "".join(generated_password)
        pyperclip.copy(password)
        password_entry.insert(0, string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_entry_get = website_entry.get()
    email_user_entry_get = email_user_entry.get()
    password_entry_get = password_entry.get()
    new_data = {
        website_entry_get: {
            "email": email_user_entry_get,
            "password": password_entry_get,
        }
    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        tkinter.messagebox.showerror(title="website", message="field left empty")
    else:
        with open("data.json", "r") as save_password:
            data = json.load(save_password)
            data.update(new_data)
        with open("data.json", "w") as save_password:
            json.dump(data, save_password, indent=4)
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
# ---------------------------- SEARCH------------------------------- #
##Write
#json.dump()
##Read
#json.load()
##Update
#json.update()
def find_password():
    password_entry.delete(0, "end")
    website_entry_get = website_entry.get()
    with open("data.json", "r") as save_password:
        data = json.load(save_password)
        password_entry.insert(0, string=data[website_entry_get]['password'])
        # if website_entry_get == data[website_entry_get]:
        #     pass_w = data[website_entry_get]["password"]
        #     password_entry.insert(0, string=pass_w)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
logo_png = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1) #g

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0) #g
email_user_label = tk.Label(text="Email/Username:")
email_user_label.grid(row=2, column=0) #g
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0) #g

website_entry = tk.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.insert(0, string="insert name of website")

email_user_entry = tk.Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_user_entry.insert(0, string="name@email.com")

password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky="EW")
password_entry.insert(0, string="")

generate_button = tk.Button(width=14, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = tk.Button(text="Search", width=14,command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()