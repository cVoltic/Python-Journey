"""Simple Class that Keep Track of the snake score"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #game over sequence
    def game_over(self):
        self.clear()
        self.write(arg=f"Game Over! Your final score is {self.score}", align=ALIGNMENT, font=FONT)
