from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


def generate_password():
    password_entry.delete(0,END)                                                     # -> clear the default screen
    letter = list(string.ascii_letters)                                                             # -> all the alphabets
    digits = list(string.digits)                                                                          # -> all the digits
    symbol = list(string.punctuation)                                                              # -> all the special symbols

    letter_count = random.randint(3,6)
    digits_count = random.randint(3,6)
    symbol_count = random.randint(3,6)

    password_list = []

    for i in range(letter_count):
        password_list.append(random.choice(letter))
    for i in range(digits_count):
        password_list.append(random.choice(digits))
    for i in range(symbol_count):
        password_list.append(random.choice(symbol))

    random.shuffle(password_list)

    password = ""
    for c in password_list:
        password += c
    password_entry.insert(0,password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={
        website:{
            "email" : email,
            "password": password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!!! ", message="Please ensure that website and password are both filled up.")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)                                                                 # load the data that is old data
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file,indent=4)

        else:
            data.update(new_data)                                                                                 # update old data
            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)                                                  # save the updated data
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email} \n password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists.")


window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas = Canvas(height= 300, width=220)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(110,150, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/ Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries / Textbox
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=54)
email_entry.insert(0, "dipanjan@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search",width=10, command=find_password)
search_btn.grid(row=1,column=2)
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3,column=2)
add_btn = Button(text="Add", width=46, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()