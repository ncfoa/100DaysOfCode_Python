from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Let's Go To The Turtle Races!")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
start = [-75, -45, -15, 15, 45, 75 ]
racing = False
all_turtles = []
winning_order = []

for t_index in range(6):
    turtle = Turtle(shape=turtle)
    turtle.color("grey", colors[t_index])
    turtle.penup()
    turtle.goto(x=-240, y=start[t_index])
    all_turtles.append(turtle)

wager = screen.textinput(title="Make Your Wager!", prompt="Which Turtle do you think will win? ").lower()

if wager:
    racing = True

while racing:
    for turtle in all_turtles:
        distance = random.randint(1, 10)

        if turtle.xcor() == 226:
            winner = turtle.pencolor()
            racing = False
            print(f"The winner is {winner}")
            if wager == winner:
                print("Congratulations, You Won!")
            else:
                print("Sorry you didn't pick the winner... ")
        else:
            while turtle.xcor() + distance > 226:
                distance = random.randint(1, 10)
            turtle.forward(distance)


screen.exitonclick()