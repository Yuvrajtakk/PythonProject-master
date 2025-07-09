import turtle
import pandas

# 1. Set up the game screen
screen = turtle.Screen()
screen.setup(width=700, height=800)
screen.title("India States & UTs Game")

# 2. Load the map image

image = "blank_indian_map.gif"
screen.addshape(image) # Add the image as a new shape
turtle.shape(image)    # Set the turtle's shape to be the map

data = pandas.read_csv("28_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

