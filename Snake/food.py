"""Food object that generate a random circle on the board"""
from turtle import Turtle
import random

# Food class inherit from Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        # generate a random coordinate for our food
        self.refresh()

    # generate a new random food location
    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)