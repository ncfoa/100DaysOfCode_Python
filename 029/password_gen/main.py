from tkinter import *
from tkinter import messagebox as mw
import random
import json


# ---------------------------- Password Generator ------------------------------- #
def generate_password():
    pw = []
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
            '#', '$', '%', '&', '*', '@']

    for i in range(10):
        num = random.randint(0, len(char) - 1)
        pw.append(char[num])
    pw = "".join(pw)
    password_entry.delete(0, END)
    password_entry.insert(0, pw)
    w.clipboard_clear()
    w.clipboard_append(pw)
    return pw


# ---------------------------- Search Password ------------------------------- #
def search():
    site = url_entry.get()

    if not site:
        mw.showwarning(message="Required Field missing.", parent=w, detail="Please ensure you have put in the Website "
                                                                           "Name.")
    else:
        try:
            with open("data.json", "r") as r:
                data = json.load(r)

        except KeyError:
            mw.showwarning(message=f"No entry for {site}.", parent=w,
                           detail=f"You do not have an entry for {site} in this application")
        except FileNotFoundError:
            mw.showwarning(message=f"Data File Not Found.", parent=w,
                           detail=f"The data file does not exist.")
            r.close()

        else:
            email_entry.delete(0, END)
            email_entry.insert(0, data[site]["email"])
            password_entry.delete(0, END)
            password_entry.insert(0, data[site]["password"])
            w.clipboard_clear()
            w.clipboard_append(data[site]["password"])


# ---------------------------- Save Password ------------------------------- #
def save_password():
    web = url_entry.get()
    em = email_entry.get()
    pw = password_entry.get()
    new_data = {}
    if not url or not email or not pw:
        mw.showwarning(message="Please fill in all fields.", parent=w, detail="You left one or more fields blank.")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            f.close()
            with open("data.json", "w") as f:
                json.dump({}, f)
                f.close()

        with open("data.json", "r") as f:
            data = json.load(f)
            f.close()

            exists = {}
        try:
            if data[web]:
                exists = data
        except KeyError:
            pass

        if exists:
            overwrite_ok = mw.askyesno(title="Continue?", message=f"{web} already has an entry",
                                       detail=f"Username: {exists[web]['email']}\n Password: {exists[web]['password']}\n"
                                              f" Do you want to overwrite?")
            if overwrite_ok:
                data.update(new_data)
        else:
            data.update(new_data)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
            f.close()
        url_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("MyPass")
w.config(padx=50, pady=50)
image = PhotoImage(file="logo.png")
c = Canvas(width=200, height=200,  highlightthickness=0)
c.create_image(100, 100, image=image)
c.grid(column=1, row=1)

url = Label(text="Website: ")
url.grid(column=0, row=3, sticky="E")
url_entry = Entry(width=35)
url_entry.focus()
url_entry.grid(column=1, row=3, sticky="E")
search_btn = Button(text="Search", width=21, command=search)
search_btn.grid(column=2, row=3)
email = Label(text="Email/Username: ")
email.grid(column=0, row=4, sticky="E")
email_entry = Entry(width=35)
email_entry.grid(column=1, row=4, columnspan=2, sticky="WE")
password = Label(text="Password: ")
password.grid(column=0, row=5, sticky="E")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=5, columnspan=2, sticky="W")
pass_btn = Button(text="Generate Password", width=21, borderwidth=4, relief="ridge", command=generate_password)
pass_btn.grid(column=2, row=5)
add_btn = Button(text="Add", command=save_password)
add_btn.grid(column=1, row=6, columnspan=2, sticky="EW")

w.mainloop()
