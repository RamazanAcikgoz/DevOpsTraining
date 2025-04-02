# We are going to use cologram.py library
# Cologram let us extract colors from images
import colorgram

# Extract 6 colors from an image.
#colors = colorgram.extract('sweet_pic.jpg', 6)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
#first_color = colors[0]
#rgb = first_color.rgb # e.g. (255, 151, 210)
#hsl = first_color.hsl # e.g. (230, 255, 203)
#proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
#red = rgb[0]
#red = rgb.r
#saturation = hsl[1]
#saturation = hsl.s
import colorgram
import turtle as turtle_module
import random

from PIL.ImageChops import screen

# Pick up colors from the image into the list
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#print(rgb_colors)

turtle_module.colormode(255)
ark = turtle_module.Turtle()
ark.speed("fastest")
ark.penup()
ark.hideturtle()
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

ark.setheading(225)
ark.forward(300)
ark.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    ark.dot(20,random.choice(color_list))
    ark.forward(50)

    if dot_counts % 10 == 0:
        ark.setheading(90)
        ark.forward(50)
        ark.setheading(180)
        ark.forward(500)
        ark.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()
