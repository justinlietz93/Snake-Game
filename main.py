from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Game window setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Bonesies Snake Game')
screen.tracer(0)

# Create objects
snake = Snake()
food = Food()
score = Scoreboard()

# Screen events
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

# Game loop and clock
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.add_segment()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
