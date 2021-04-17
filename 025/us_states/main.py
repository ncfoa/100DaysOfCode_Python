import turtle
import pandas

screen = turtle.Screen()
screen.title("How many states do you know?")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.ht()
writer.penup()

data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = turtle.textinput(title="Guess a state name", prompt="Enter a state name:").title()

    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)







screen.exitonclick()


