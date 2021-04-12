from turtle import Turtle, Screen


art = Turtle()
screen = Screen()


def move_forward():
    art.forward(10)


def move_backward():
    art.backward(10)


def turn_left():
    heading = art.heading()
    art.setheading(heading + 10)


def turn_right():
    heading = art.heading()
    art.setheading(heading - 10)


def clear():
    art.goto(0,0)
    art.clear()

screen.title("Etch-a-Sketch")
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
