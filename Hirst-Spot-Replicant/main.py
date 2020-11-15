"""Replicate the Hirst Spot Image"""
import colorgram
import random
from turtle import Turtle, Screen

def make_art(pen, colors, width=10, height=10):
    # Set up the grid
    # make a size 20 dot with 50 spaces apart

    for i in range(height):
        # get the current position
        current_pos = pen.pos()
        for j in range(width):
            # choose a randome color, place a dot and move forward
            pen.dot(20,random.choice(colors))
            pen.penup()
            pen.forward(50)
            pen.pendown()

        #now move up a row
        pen.penup()
        pen.setx(current_pos[0])
        pen.sety(current_pos[1]+50)


if __name__ == "__main__":
    #Extract all color from your image
    colors = colorgram.extract("hirst-image.jpg", 30)
    colors_list = [tuple(color.rgb) for color in colors ]


    #create the pen turtle object and begin making the art piece
    pen = Turtle()

    #set up the cursor
    pen.hideturtle()
    pen.setheading(225)
    pen.penup()
    pen.forward(300)
    pen.setheading(0)
    pen.down()
    pen.speed('fastest')

    screen = Screen()
    screen.colormode(255)
    make_art(pen, colors_list)
    screen.exitonclick()