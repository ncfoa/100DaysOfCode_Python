# Art by turtle...

from turtle import Turtle as T, Screen as S
import random

art = T()
art.shape("turtle")
art.color("black", "green")
art.pencolor("#"+''.join(random.choice('0123456789ABCDEF') for j in range(6)))
screen = S()


# Draw a Square

# for _ in range(4):
#     for i in range(10):
#         art.forward(10)
#         art.penup()
#         art.forward(10)
#         art.pendown()
#     art.right(90)
#     art.pencolor("#" + ''.join(random.choice('0123456789ABCDEF') for j in range(6)))

# End Draw a Square

### Begin Draw Shapes.

# def draw(sides):
#     angle = 360 / sides
#     art.pencolor("#" + ''.join(random.choice('0123456789ABCDEF') for j in range(6)))
#     for _ in range(sides):
#         art.forward(100)
#         art.right(angle)
#
#
# for shape in range(3, 11):
#     draw(shape)

###  End Draw Shapes.


### Start Random Walk.

# def random_walk(degrees):
#     art.pencolor("#" + ''.join(random.choice('0123456789ABCDEF') for j in range(6)))
#     art.setheading(degrees)
#     art.forward(30)
#
#
# art.speed("fastest")
# art.pensize(15)
#
# for _ in range(200):
#
#     degrees = [0, 90, 180, 270]
#     random_walk( random.choice(degrees))

### End Random Walk.

### Begin Spirograph.

art.speed("fastest")
art.hideturtle()


def circle():
    art.circle(100)

# change width to number between 10 an 360 for density of spirograph
width = 5


for _ in range(width):
    art.pencolor("#" + ''.join(random.choice('0123456789ABCDEF') for j in range(6)))
    circle()
    art.left(360 / width)

### End Spirograph


screen.exitonclick()