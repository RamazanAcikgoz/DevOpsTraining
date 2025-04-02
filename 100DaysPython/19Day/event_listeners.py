from turtle import Turtle, Screen

ark = Turtle()
screen = Screen()

def move_forwards():
    ark.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards) #function used as input and we cannot use () in such a usage
screen.exitonclick()

