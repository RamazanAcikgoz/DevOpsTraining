import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class BlockManager(Turtle):

    def __init__(self):
        self.all_blocks = []
        self.block_speed = STARTING_MOVE_DISTANCE

    def add_block(self):
        random_chance = random.randint(1,7)
        if random_chance == 1:
            new_block = Turtle("square")
            new_block.color(random.choice(COLORS))
            new_block.penup()
            new_block.shapesize(stretch_wid=1, stretch_len=3)
            random_y = random.randint(-250,250)
            new_block.goto(325,random_y)
            self.all_blocks.append(new_block)

    def move_blocks(self):
        #Move blocks
        for block in self.all_blocks:
            block.backward(self.block_speed)

    def level_up(self):
        self.block_speed += MOVE_INCREMENT


