import turtle
import pandas

# def get_mouse_click_coor(x , y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


# Screen setup
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# States dictionary
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # data.state(column) will be into the list
guessed_states = []


# 4. Use a loop to allow the user to keep guessing
while len(guessed_states) < 50: # 6. Keep track of the score
    # 1. Convert the guess to Title case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:  # # 2. Check if the guess is among the 50 states 3. Write correct guesses onto the map
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # It will take whole row
        t.goto(state_data.x.item(), state_data.y.item()) # state_data.x and y will read x and y columns (item() is help to accessing in column)
        t.write(answer_state)

