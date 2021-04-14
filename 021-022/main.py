from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PONG!")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="a", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()

    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.paddle_hit()

    if ball.xcor() > 370:
        score_board.increase_l_score()
        ball.reset_game()

    if ball.xcor() < -370:
        score_board.increase_r_score()
        ball.reset_game()

    if score_board.l_score == 5 or score_board.r_score == 5:
        game_on = False
        score_board.determine_winner()

screen.exitonclick()
