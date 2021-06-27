import time
from tkinter import *
from tkmacosx import Button as btn
from tkinter import scrolledtext
import math

WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#ff0000"
GOLD = "#d3bc8d"
FONT = "Courier"
timer = None


# Timer
def start_timer():
    time.sleep(2)
    text.focus()
    w.after(3000, lt.config(text="GO!"))
    count_down(60)


# CountDown
def count_down(n):

    count_s = "{:02d}".format(n % 60)
    c.itemconfigure(txt, text=f"{count_s}")
    if n > 0:
        global timer
        timer = w.after(1000, count_down, n - 1)
    else:
        words = text.get('1.0', END)
        lw = len(words)
        wpm = lw / 5
        lt.config(text=f"You typed {wpm} words per minute!")


instructions = '''Press the start button when ready. You will have 3 seconds to prepare to start typing. 
Use the following sentences during the test if you finish with the last sentence start from the top again. '''
sentences = '''
The quick brown fox jumped over the lazy dog.
My girl wove six dozen plaid jackets before she quit.
A wizard’s job is to vex chumps quickly in fog.
When zombies arrive, quickly fax Judge Pat.
Pack my box with five dozen liquor jugs.'''

# UI SETUP
w = Tk()
w.title("Words Per Minute")
w.config(padx=100, pady=50, bg=BLACK)
i = Label(fg=GOLD, bg=BLACK, font=(FONT, 15, "bold"), text=instructions)
i.grid(column=1, row=0)
i2 = Label(fg=WHITE, bg=BLACK, font=(FONT, 15, "bold"), text=sentences)
i2.grid(column=1, row=1)
lt = Label(fg=GOLD, bg=BLACK, font=(FONT, 40, "bold"), text="Get Ready")
lt.grid(column=1, row=2)
c = Canvas(width=200, height=224, bg=BLACK, highlightthickness=0)
txt = c.create_text(100, 120, text="60", fill="white", font=(FONT, 35, "bold"))
c.grid(column=1, row=3)
sb = btn(w, text="START", bg=GOLD, fg=BLACK, borderless=1, command=start_timer)
sb.grid(column=1, row=4)
text = scrolledtext.ScrolledText(w, height=8, width=40)
scroll = Scrollbar(w)
text.configure(yscrollcommand=scroll.set)
text.grid(column=1, row=5)
text.insert(END, "")


w.mainloop()
