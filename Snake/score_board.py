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
        # read the highscore recorded from a file
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    # reset the scoreboard and update the high score if neccessary
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # write the highscore in a file
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))
        # reset the current score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    # #game over sequence
    # def game_over(self):
    #     self.clear()
    #     self.write(arg=f"Game Over! Your final score is {self.score}", align=ALIGNMENT, font=FONT)
