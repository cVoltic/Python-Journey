"""Simple Snake Game"""
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
# for animation purposes
import time

if __name__ == "__main__":
    # instantiate a screen class, exit on click
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    #turn the animation off initially
    screen.tracer(0)

    snake = Snake() # OOP build the snake
    food = Food()   # OOP generate a food item
    score_board = ScoreBoard()  #OOP generate the score

    # enable event listener
    # give the snake a way to move according to keystroke
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
        snake.move()    # move the snake forward

        # detect collision using distances between the snake head and the food item
        # add to the snake if the snake eat the food
        if snake.head.distance(food) < 15:
            food.refresh()
            score_board.increase_score()
            snake.extend()

        # detect collision with wall (our board is 600 x 600) or +/- 300 each and snake has a side of 20
        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
            score_board.reset()
            snake.reset()

        # detect the collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score_board.reset()
                snake.reset()

    screen.exitonclick()