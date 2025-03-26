from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
tom = Turtle()
tom.shape("turtle")
# color
tom.color("brown")

for _ in range(4):
    tom.forward(100)
    tom.right(90)












# Screen will keep open the window until click on it
screen = Screen()
screen.exitonclick()

