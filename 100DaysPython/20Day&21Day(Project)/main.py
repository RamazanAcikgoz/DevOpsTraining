# Snake Game
#
# 1. Create a snake body +
# 2. Move the snake +
# 3. Create snake food
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.bgcolor("Black")
screen.setup(width= 600, height= 600)
screen.title("My Snake Game")
screen.tracer(0)

# Snake - Food - Scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control of snake
screen.listen()
screen.onkey(snake.up, key = "Up")
screen.onkey(snake.down, key = "Down")
screen.onkey(snake.right, key = "Right")
screen.onkey(snake.left, key = "Left")


# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.squares:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()