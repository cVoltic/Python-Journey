"""Handle Scoring for either player"""
from turtle import Turtle

class ScoreBoard(Turtle):
    # constructor
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    # render the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 88, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 88, "normal"))

    # award point
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # award point
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()