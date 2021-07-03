from tkinter import *

BACKGROUND_COLOR = "#6f96bd"
count = 5
active = 0


def activity(event=None):
    global active
    active += 1


def timer():
    global count
    global active
    count -= 1
    if count == 0:
        count = 5
        if active == 0:
            text.delete("1.0", END)
            count = 5
        w.after(1000, timer)
        active = 0
    else:
        w.after(1000, timer)


# Window Creation
w = Tk()
w.title("Writers Block Aid")
w.minsize(width=850, height=590)
w.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Labels
label_title = Label(text="Writers Block Aide", font=("Ariel", 50), foreground="white",
                    background=BACKGROUND_COLOR, pady=5)
label_title.grid(column=1, row=1)

label_directions = Label(text="Click Start and Start Typing! If you pause for more than 5 seconds, your text "
                              "will disappear!", font=("Ariel", 20), foreground="black", background=BACKGROUND_COLOR,
                         pady=30)
label_directions.grid(column=1, row=2)
frame = Frame(w)
frame.grid(column=1, row=3)
start_button = Button(frame, text="Start", font=('Arial', 24), width=21, borderwidth=4, relief="ridge",
                      activebackground="#6f96bd", command=timer)
start_button.grid(column=1, row=3)
start_button.focus_set()
text = Text(height=15, width=40, font=("courier", 20))
text.focus()
text.config(wrap=WORD)
text.grid(column=1, row=5, pady=(10, 0))

w.bind("<Key>", activity)
w.mainloop()
