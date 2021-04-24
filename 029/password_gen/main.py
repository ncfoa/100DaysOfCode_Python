from tkinter import *
from tkinter import messagebox as mw
import random


# ---------------------------- Password Generator ------------------------------- #
def generate_password():
    pw = []
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
            '#', '$', '%', '&', '*', '@']
    print(len(char))
    for i in range(10):
        num = random.randint(0, len(char) - 1)
        pw.append(char[num])
    pw = "".join(pw)
    password_entry.delete(0, END)
    password_entry.insert(0, pw)
    w.clipboard_clear()
    w.clipboard_append(pw)
    return pw


# ---------------------------- Save Password ------------------------------- #
def save_password():
    web = url_entry.get()
    em = email_entry.get()
    pw = password_entry.get()
    print(web)
    if not url or not email or not pw:
        mw.showwarning(message="Please fill in all fields.", parent=w, detail="You left one or more fields blank.")
    else:
        is_ok = mw.askyesno(title="My Title", message=f"{web}", detail=f"You entered: \n Username: {em} \n Password:"
                                                                       f" {pw} \n Is this ok?")
        if is_ok:
            with open("./passwords.txt", "a") as f:
                f.write(f"{web} | {em} | {pw} \n")
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
url_entry.grid(column=1, row=3, columnspan=2, sticky="E")
email = Label(text="Email/Username: ")
email.grid(column=0, row=4, sticky="E")
email_entry = Entry(width=35)
email_entry.grid(column=1, row=4, columnspan=2, sticky="E")
password = Label(text="Password: ")
password.grid(column=0, row=5, sticky="E")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=5, sticky="W")
pass_btn = Button(text="Generate Password", command=generate_password)
pass_btn.grid(column=2, row=5)
add_btn = Button(text="Add", command=save_password)
add_btn.grid(column=1, row=6, columnspan=2, sticky="EW")

w.mainloop()
