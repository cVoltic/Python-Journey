"""Render a paddle to play pong"""
from turtle import Turtle


class Paddle(Turtle):
    # constructor
    def __init__(self, starting_pos=()):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_pos)

    # move the paddle to new up position
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # move the paddle to new down position
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

