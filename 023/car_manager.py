from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.row = 0
        self.car_list = []
        self.ht()
        self.penup()

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.st()
            car.penup()
            car.shape("square")
            self.row = -250 + (random.randint(0, 24) * 20)
            car.goto(280, self.row)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.move_distance)

    def next_level(self):
        self.move_distance += MOVE_INCREMENT

