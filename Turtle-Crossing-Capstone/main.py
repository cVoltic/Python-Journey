from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time


if __name__ == '__main__':
    # instantiate screen
    # set up the width and height
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = ScoreBoard()
    # enable player movement on click

    screen.listen()
    screen.onkey(player.move, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        # let's create some car on refresh
        car_manager.create_car()
        car_manager.move_car()

        if player.is_at_finish_line():
            player.restart()
            scoreboard.level_up()
            car_manager.update_speed()

        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()

