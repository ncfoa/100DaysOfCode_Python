from turtle import Turtle as T, Screen as S
import random

art = T()
art.shape("turtle")
screen = S()

def random_color():
    color = "#" + ''.join(random.choice('0123456789ABCDEF') for j in range(6))

    while color == "#FFFFFF" or color == "#000000":
        color = "#" + ''.join(random.choice('0123456789ABCDEF') for j in range(6))

    return color


# def bounds(rows, columns):
#     size = str(screen.screensize()).replace("(", "").replace(")", "").split(',')
#     width = int(size[0])
#     height = int(size[1])
#
#     h_spaces = width / rows
#     l_spaces = height / columns
#     return [h_spaces, l_spaces]

def draw_row(num_dots):
    for _ in range(num_dots):
        art.dot(20, random_color())
        art.forward(50)
    art.setheading(90)
    art.forward(50)
    art.setheading(180)
    art.forward(750)
    art.setheading(0)


def draw(num_rows, num_columns):
    screen.title("Damien Hirst Dots Painting")
    screen.bgcolor("black")
    art.hideturtle()
    art.speed("fastest")
    art.penup()
    art.setheading(225)
    for _ in  range(10):
        # art.penup()
        art.forward(50)
    art.setheading(0)
    for _ in range(num_rows):
        draw_row(num_columns)

draw(15, 15)

screen.exitonclick()