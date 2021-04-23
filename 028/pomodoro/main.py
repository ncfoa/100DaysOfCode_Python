from tkinter import *
from tkmacosx import Button as btn
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
CHECK = "✔"
reps = 0
chk = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    global reps
    global chk
    reps = 0
    chk = 0
    c.itemconfigure(txt, text="00:00")
    lt.config(text="Timer", fg=GREEN)
    lc.config(text="")
    w.after_cancel(timer)
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global chk
    reps += 1
    if reps % 8 == 0:
        chk = 0
        count_down(LONG_BREAK_MIN * 60)
        lt.config(text="Break", fg=RED)
        lc.config(text="")
    elif reps % 2 == 0:
        chk += 1
        chks = ""
        for _ in range(chk):
            chks = chks + CHECK
        lc.config(text=chks)
        count_down(SHORT_BREAK_MIN * 60)
        lt.config(text="Break", fg=PINK)

    else:
        count_down(WORK_MIN * 60)
        lt.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(n):
    count_m = "{0:0=2d}".format(math.floor(n / 60))
    count_s = "{0:0=2d}".format(n % 60)
    c.itemconfigure(txt, text=f"{count_m}:{count_s}")
    if n > 0:
        global timer
        timer = w.after(1000, count_down, n - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Pomodoro")
w.config(padx=100, pady=50, bg=YELLOW)
image = PhotoImage(file="tomato.png")
c = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
c.create_image(100, 110, image=image)

txt = c.create_text(100, 120, text="00:00", fill="white", font=(FONT, 35, "bold"))
c.grid(column=1, row=1)
lt = Label(fg=GREEN, bg=YELLOW, font=(FONT, 50, "bold"), text="Timer")
lt.grid(column=1, row=0)
sb = btn(text="START", bg=YELLOW, fg="blue", borderless=1, command=start_timer)
sb.grid(column=0, row=2)
lc = Label(fg=GREEN, bg=YELLOW, font=(FONT, 35, "bold"), text=" ")
lc.grid(column=1, row=3)
rb = btn(text="RESET", bg=YELLOW, fg="blue", borderless=1, command=reset)
rb.grid(column=2, row=2)
w.mainloop()