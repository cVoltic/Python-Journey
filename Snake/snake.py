"""Snake Object"""
from turtle import Turtle

#Global starting postion
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

#Snake should not be able to move back and forth on itself
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # snake constructor => build the snake on screen when snake class is instantiated
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle(shape='square')
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    # propel the snake forward
    def move(self):
        # update the seg+1 position to seg postion until loop is complete
        for seg in range(len(self.segments) - 1, 0, -1):
            # get the front segment
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # enable the snake to turn according to keypresses
    # the snake cannot go back and forth into itself!
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # increase the snake length by 1
    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    # reset the snake when it dies
    # reinit the snake at origin
    def reset(self):
        # before we clear the snake, we need to move the rest of
        # the snake off screen
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]


    def extend(self):
        self.add_segment(self.tail.position())
