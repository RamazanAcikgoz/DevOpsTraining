import random
from turtle import Turtle, Screen

ark = Turtle()
ark.shape("turtle")
ark.color("black")
ark.width(3)
#ark.pensize(15)



colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


for _ in range(200):
    ark.color(random.choice(colours))
    ark.forward(30)
    ark.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()