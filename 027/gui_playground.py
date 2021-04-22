from tkinter import *


def reset():
    label["text"] = "Hello World"


def button_click():
    label["text"] = "OMG YOU CLICKED IT!"


def display_text():

    label["text"] = text.get()


# Create window
w = Tk()
w.title("Dave's Window")
w.minsize(width=800, height=600)
w.config(padx=20, pady=20)
# Create border
frame = Frame(w, borderwidth=5, relief=SUNKEN)
frame.grid(column=0, row=2)
# Create Label
label = Label(text="Hello World!", font=("Arial", 24, "bold"))
label.grid(column=2, row=0)
label.config(padx=5, pady=5)
# Create Text Entry Box
text = Entry(frame, borderwidth=5, relief=FLAT)
text.grid(column=0, row=2)
text.insert(END, "What are you doing?")
# Create Buttons
button = Button(text="click me...", command=button_click)
button.grid(column=2, row=2)
display_button = Button(text="display", command=display_text)
display_button.grid(column=1, row=2)
reset_button = Button(text="reset", command=reset)
reset_button.grid(column=3, row=3)

w.mainloop()
