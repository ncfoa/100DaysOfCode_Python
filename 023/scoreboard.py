from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-150, 265)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        fs = 24
        for i in range(24, 61):
            fs += 1
            self.clear()
            self.goto(-150, 265)
            self.write(f"Level: {self.level}", align="center", font=FONT)
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=("Courier", fs, "normal"))
            time.sleep(.05)

        for i in range(24, 61):
            fs -= 1
            self.clear()
            self.goto(-150, 265)
            self.write(f"Level: {self.level}", align="center", font=FONT)
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=("Courier", fs, "normal"))
            time.sleep(.05)
