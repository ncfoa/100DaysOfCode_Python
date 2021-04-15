from turtle import Turtle
import json

FONT = ("Arial", 24, "normal")
FILE_NAME = "high_score.json"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.high_score = {"high_score": 0}
        self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 270)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(150, 270)
        if self.score > self.high_score["high_score"]:
            self.high_score["high_score"] = self.score
        self.write(f'High Score: {self.high_score["high_score"]}', align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.write_high_score()

    def read_high_score(self):
        try:
            with open(FILE_NAME, 'r') as fr:
                previous_results = fr.read()
                fr.close()
                print(previous_results)
                self.high_score = json.loads(previous_results)
        except FileNotFoundError:
            with open(FILE_NAME, 'w') as fw:
                self.high_score = {"high_score": 0}
                hs = json.dumps(self.high_score)
                fw.write(hs)


    def write_high_score(self):
        with open(FILE_NAME, "w") as fc:
            fc.write(json.dumps(self.high_score))
            fc.close()
