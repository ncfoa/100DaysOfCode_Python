import random
from tkinter import *


words_list = []
try:
    with open("data/words_to_learn.csv", "r") as j:
        words = j.read()
        j.close()
except FileNotFoundError:
    with open("./data/japanese.csv", "r") as j:
        japanese = j.read()
        j.close()

    with open('./data/known_words.csv', "w") as k:
        k.close()

    for i in japanese.split("\n"):
        with open("./data/words_to_learn.csv", "a") as f:
            words_list.append(i.split(","))
            f.write(f"{i}\n")
    f.close()
else:
    for i in words:
        n = words.split("/n")
        # noinspection PyUnresolvedReferences
        words_list.append(n.split(","))


rand_num = ''


# Generate Random Japanese Word
def get_word():
    global words_list, rand_num
    rand_num = random.randint(0, len(words_list))
    word = words_list[rand_num]
    print(word)
    print(len(words_list))
    return word


#  Check answer
# noinspection PyUnresolvedReferences
def check_answer(back):
    global card_back, c
    w.after(5000)
    c.delete("all")
    c.create_image(400, 263.5, image=card_back)
    c.create_text(400, 200, text=f"{back[0]}", font=("Arial", 60, "bold"))
    c.create_text(400, 300, text=f"{back[1]}", font=("Arial", 60, "bold"))
    w.update()


# noinspection PyUnresolvedReferences
def show_word(word):
    global card_front, c

    front = word
    c.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))
    c.create_text(400, 250, text=f"{front[0]}", font=("Arial", 60, "bold"))
    c.create_text(400, 320, text=f"({front[2]})", font=("Arial", 40, "normal"))
    w.update()
    check_answer(front)


def know_click():
    global words_list, rand_num, kanji, data, c
    # noinspection PyTypeChecker
    word = words_list[rand_num]
    with open("data/words_to_learn.csv", "w") as q:
        # noinspection PyTypeChecker
        words_list.pop(rand_num)
        for b in words_list:
            print(b)
            q.write(f"{b}\n")
        q.close()
    with open("data/known_words.csv", "a") as a:
        a.write(f"{word}\n")
        a.close()

    c.delete("all")
    kanji = ''
    start()


def dont_know_click():
    global kanji, c
    c.delete("all")
    kanji = ''
    start()


def start():
    global data, card_front, c, kanji
    kanji = get_word()
    c = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
    c.create_image(400, 263.5, image=card_front)
    c.grid(column=0, row=0, columnspan=2, sticky="WE")
    x_btn = Button(text="x", image=x_img, bd=0, bg="#B1DDC6", highlightthickness=0, command=dont_know_click)
    x_btn.grid(column=0, row=1, padx=20, pady=20)
    y_btn = Button(text="y", image=y_img, bd=0, bg="#B1DDC6", highlightthickness=0, command=know_click)
    y_btn.grid(column=1, row=1, padx=20, pady=20)
    show_word(kanji)


# Build GUI for App
w = Tk()
w.title("Learn Japanese")
w.config(bg="#B1DDC6", padx=50, pady=50)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
f_img = PhotoImage(file="./images/wrong.png")
t_img = PhotoImage(file="./images/right.png")
c = ''
kanji = ''
data = []
start()



w.mainloop()
