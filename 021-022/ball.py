from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x=x_new, y=y_new)

    def bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_hit()
