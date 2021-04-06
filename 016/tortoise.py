from turtle import Turtle, Screen


slow_poke = Turtle()

slow_poke.shape("turtle")
slow_poke.color( "blue", "green")

the_screen = Screen()
the_screen.title("Dave's Turtle")
# the_screen.setup(250, 250)
# slow_poke.penup()
# slow_poke.goto(-100,0)
# slow_poke.pendown()
slow_poke.begin_fill()
while True:
    slow_poke.forward(200)
    slow_poke.left(170)
    if abs(slow_poke.pos()) < 1:
        break
slow_poke.end_fill()
print(the_screen.screensize())
the_screen.exitonclick()

