import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score_board = Scoreboard()
player = Player()
car_manager = CarManager()
game_on = True
screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
loop_num = 0
while game_on:
    time.sleep(0.1)
    screen.update()
    loop_num += 1

    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_on = False
            score_board.game_over()

    if player.ycor() == player.finish_line:
        score_board.level += 1
        score_board.next_level()
        player.next_level()
        car_manager.next_level()


screen.exitonclick()
