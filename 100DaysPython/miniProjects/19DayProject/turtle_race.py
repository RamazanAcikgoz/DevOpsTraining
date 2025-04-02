import random
import turtle
from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "black", "green", "blue", "purple"]
y_position = [90, 60, 30, 0, -30, -60]
all_turtlest = []

# Turtles
for turtle_position in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_position])
    new_turtle.goto(x = -230, y = y_position[turtle_position])
    all_turtlest.append(new_turtle)



# forwards
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtlest:
        if turtle.xcor() > 230:
            is_race_on = False
            screen.clear()
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()