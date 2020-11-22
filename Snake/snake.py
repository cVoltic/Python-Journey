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
        self.__snake = []
        self.__segment = None
        self.create_snake()
        self.__head = self.__snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.__segment = Turtle(shape='square')
            self.__segment.color("white")
            self.__segment.penup()
            self.__segment.goto(position)
            self.__snake.append(self.__segment)

    # propel the snake forward
    def move(self):
        # update the seg+1 position to seg postion until loop is complete
        for seg in range(len(self.__snake) - 1, 0, -1):
            # get the front segment
            new_x = self.__snake[seg - 1].xcor()
            new_y = self.__snake[seg - 1].ycor()
            self.__snake[seg].goto(new_x, new_y)
        self.__snake[0].forward(MOVE_DISTANCE)

    # enable the snake to turn according to keypresses
    # the snake cannot go back and forth into itself!
    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)
