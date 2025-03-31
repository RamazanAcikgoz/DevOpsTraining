# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
import random
from turtle import Turtle, Screen

ark = Turtle()
ark.shape("turtle")
ark.color("black")
ark.width(3)

#def triangle():
#    ark.forward(100)
#    ark.right(120)
#    ark.forward(100)
#    ark.right(120)
#    ark.forward(100)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        ark.forward(100)
        ark.right(angle)

for shape_side_n in range(3,11):
    ark.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()