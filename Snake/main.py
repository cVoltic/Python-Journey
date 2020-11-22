"""Simple Snake Game"""
from turtle import Turtle, Screen
from snake import Snake

# for animation purposes
import time

if __name__ == "__main__":
    # instantiate a screen class, exit on click
    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    #turn the animation off initially
    screen.tracer(0)

    snake = Snake() # OOP build the snake

    # enable event listener
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # working out animation
    game_is_on = True
    while game_is_on:
        # only update when every segment is moved forward
        screen.update()
        time.sleep(0.1)
        # move the snake forward
        snake.move()

    screen.exitonclick()