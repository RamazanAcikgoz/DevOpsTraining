# Turtle crossing
#
# 1. Create random cars/blocks with random calors and speeds
# 2. Create a turtle/player
# 3. Add turtle control
# 4. After finish the cross reset turtle position (Turtle will wait a 2 second and reset the position)
# 5. If turtle hit the car it is GAME OVER
# 6. Level up and change difficulties

import time
from turtle import Screen
from player import Player
from block_manager import BlockManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Turtle cross")
screen.tracer(0)



# Player control
player_turtle = Player()
screen.listen()
screen.onkey(player_turtle.go_up, key = "Up")
screen.onkey(player_turtle.clear, key = "c")

# Scoreboard
scoreboard = Scoreboard()

# Car
blocks = BlockManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    blocks.add_block()
    blocks.move_blocks()

    # Finish line
    if player_turtle.is_that_finish_line():
        time.sleep(1)
        scoreboard.increase_level()
        blocks.level_up()
        player_turtle.start_position()

    for block in blocks.all_blocks:
        if block.distance(player_turtle) < 20:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()