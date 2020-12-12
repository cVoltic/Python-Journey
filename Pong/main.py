from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time



if __name__ == "__main__":
    #create screen
    screen = Screen()
    screen.setup(width=800,height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    # Turn the render animation off initially
    screen.tracer(0)


    net = Turtle()
    net.color("white")
    net.pensize(10)
    net.shape("square")
    net.setheading(270)
    net.penup()
    net.goto(0, 400)
    while net.ycor() > -400:
        net.pendown()
        net.forward(20)
        net.penup()
        net.forward(20)
    net.goto(0, 400)

    paddle_r = Paddle((350, 0))
    paddle_l = Paddle((-350, 0))
    ball = Ball()
    scoreboard = ScoreBoard()

    # move up and down
    screen.listen()

    screen.onkeypress(paddle_r.up, "Up")
    screen.onkeypress(paddle_r.down, "Down")

    screen.onkey(paddle_l.up, "w")
    screen.onkey(paddle_l.down, "s")


    # let the paddle render
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        ball.move()
        # ball wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # detect collision with right paddle
        if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # detect when the ball is out of bound when either player misses
        if ball.xcor() > 400:
            scoreboard.l_point()
            ball.restart()

        if ball.xcor() < -400:
            scoreboard.r_point()
            ball.restart()

    screen.exitonclick()