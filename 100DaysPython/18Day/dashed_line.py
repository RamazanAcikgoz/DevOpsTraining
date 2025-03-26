from turtle import Turtle, Screen

tom = Turtle()
tom.shape("arrow")
tom.color("black")
tom.width(3)

for _ in range(20):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()




screen = Screen()
screen.exitonclick()

