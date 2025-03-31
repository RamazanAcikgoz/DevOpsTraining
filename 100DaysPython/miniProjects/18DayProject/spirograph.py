import random
from turtle import Turtle, Screen

ark = Turtle()
ark.shape("turtle")
ark.color("black")
#ark.width(3)
ark.speed("fastest")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(200):
    ark.color(random.choice(colours))
    ark.circle(100)
    #ark.heading()
    #ark.forward(10)
    ark.right(10)
