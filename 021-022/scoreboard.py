from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white", "white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        for i in range(0, int(600 / 40)):
            self.seth(270)
            self.shape("square")
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.goto(-150, 230)
        self.write("Player 1", align="right", font=("Courier", 20, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(150, 230)
        self.write("Player 2", align="left", font=("Courier", 20, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()


    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def determine_winner(self):
        self.goto(0, 0)
        if self.l_score == 5:
            self.write("Player 1 has won this round..", align="center", font=("Courier", 35, "normal"))
        else:
            self.write("Player 1 has won this round..", align="center", font=("Courier", 35, "normal"))
