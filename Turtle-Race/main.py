from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# Set the screen dimension
screen.setup(width=500, height=400)
# ask the user to place their bet
user_bet = screen.textinput(title="Make your bet!", prompt="What color is your turtle for the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
#create a color turtle and position them accordingly
start_y = -100
for color in colors :
    # instantiate a turtle and position them accordingly
    Tim = Turtle(shape="turtle")
    Tim.penup()
    Tim.goto(x=-230,y=start_y)
    Tim.color(color)
    start_y+=40
    all_turtles.append(Tim)

#start the race only if the user place their bet
if user_bet:
    is_race_on = True
while is_race_on:
    # when a turtle reach the end, that turtle is a winner,
    # check to see if it is the user color
    for turtle in all_turtles:
        #get the xy_position
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.color()[0]==user_bet:
                print("Your turtle is the winner!")
            else:
                print(f"{turtle.color()[0]} turtle is the winner.")

    # randomly move a turtle forward
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()