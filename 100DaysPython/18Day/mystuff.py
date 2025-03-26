from turtle import Turtle, Screen

tom = Turtle()
tom.shape("arrow")
tom.color("black")
tom.width(3)

tom.forward(100)
tom.left(120)
tom.forward(100)
tom.left(120)
tom.forward(100)


for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tom.color(c)
        tom.forward(steps)
        tom.right(30)






screen = Screen()
screen.exitonclick()