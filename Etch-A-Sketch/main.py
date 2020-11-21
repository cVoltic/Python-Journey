from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_ccw():
    tim.lt(10)


def rotate_cw():
    tim.rt(10)

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=rotate_ccw)
screen.onkey(key="d",fun=rotate_cw)
screen.onkey(key="c",fun=tim.reset)
screen.exitonclick()