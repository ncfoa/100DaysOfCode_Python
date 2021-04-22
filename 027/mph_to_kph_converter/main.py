from tkinter import *


def convert():
    m = float(text.get())
    m *= 1.609
    m = "%.2f" % m
    km2["text"] = str(m)


def focus(event):
    text.selection_range(0, END)


# Create window
w = Tk()
w.title("MPH to KPH Converter")
w.minsize(width=200, height=100)
w.config(padx=20, pady=20)
# Create border

# Create Label
miles = Label(text="MPH", font=("Arial", 18, "bold"))
miles.grid(column=2, row=0)
miles.config(padx=5, pady=5)
km = Label(text="KPH", font=("Arial", 18, "bold"))
km.grid(column=2, row=1)
km.config(padx=5, pady=5)
equal = Label(text="is equal to", font=("Arial", 18, "bold"))
equal.grid(column=0, row=1)
equal.config(padx=5, pady=5)
km2 = Label(text="0.00", font=("Arial", 18, "bold"))
km2.grid(column=1, row=1)
km2.config(padx=5, pady=5)

# Create Text Entry Box
text = Entry(borderwidth=1, relief=SUNKEN, width=10)
text.grid(column=1, row=0)
text.insert(END, "0")
text.bind("<FocusIn>", focus)
# Create Buttons
button = Button(text="Convert", command=convert)
button.grid(column=1, row=3)


w.mainloop()