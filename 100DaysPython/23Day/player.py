from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.shapesize(1.2)
        self.setposition(STARTING_POSITION)
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        #new_y = self.ycor() + MOVE_DISTANCE
        #self.goto(self.xcor(), new_y)

    def is_that_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_position(self):
        self.goto(STARTING_POSITION)
