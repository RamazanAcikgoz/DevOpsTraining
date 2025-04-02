from turtle import Turtle, Screen

ark = Turtle()
screen = Screen()

def move_forwards():
    ark.forward(25)

def move_backwards():
    ark.backward(25)

def move_right():
    #ark.right(10)
    new_heading = ark.heading() + 10
    ark.setheading(new_heading)

def move_left():
    #ark.left(10)
    new_heading = ark.heading() - 10
    ark.setheading(new_heading)

def clear():
    ark.clear()
    ark.penup()
    ark.home()
    ark.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()