"""Simple GUI proj using turtle"""
from turtle import Turtle, Screen
import random

def change_color(pen):
    R = random.random()
    G = random.random()
    B = random.random()
    pen.color(R, G, B)

def draw_shape(num_sides):
    angle = 360 / num_sides
    change_color(timmy)
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def random_walk(steps, pen):
    pen.pensize(10)
    pen.speed('fast')
    for i in range(steps):
        #change color
        #make a random step
        #move forward after a direction change
        change_color(pen)
        pen.setheading(random.choice([0,90,180,270]))
        pen.forward(30)


def make_spirograph(pen,tilt_size):
    pen.speed('fastest')

    for i in range(360//int(tilt_size)):
        pen.circle(100)
        change_color(pen)
        pen.setheading(pen.heading() + int(tilt_size))


if __name__ == '__main__':
    # Instantiate an object and define it shape
    timmy = Turtle()
    timmy.shape('turtle')
    timmy.color('orange')

    # # Draw a square
    # for i in range(0,4):
    #     timmy.right(90)
    #     timmy.forward(100)
    #
    # # draw a dashes
    # for i in range(0,50):
    #     timmy.forward(10)
    #     timmy.penup()
    #     timmy.forward(10)
    #     timmy.pendown()

    # nested shape
    # for num_sides in range(3, 12):
    #     draw_shape(num_sides)

    # random_walk(100, timmy)

    # make_spirograph(timmy,5)


    # Enable screen and only exit when we click on the screen
    screen = Screen()
    screen.exitonclick()
