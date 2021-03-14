import turtle
import pandas as pd
import time
# start new turtle instance
screen = turtle.Screen()
screen.title("US State Game")

# start a new shape and import an image file into turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# function to write the state
def write_state(name, coor, turtle_obj):
    turtle_obj.goto(coor[0], coor[1])
    turtle_obj.write(name)

# prompt user input
state_data = pd.read_csv("50_states.csv")
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
turtle.tracer(0, 0)
guessed_state = []
while len(guessed_state) < 50:
    time.sleep(0.1)
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_state)}/50",
                                    prompt="What's another state's name?")

    if answer_state.title() == "Exit":
        all_states = list(state_data.state)
        states_to_learn = [state for state in all_states if state not in guessed_state]
        states_to_learn_data = {"state": states_to_learn}
        learn = pd.DataFrame(states_to_learn_data)
        learn.to_csv("states_to_learn.csv")
        break

    correct_state = state_data[state_data.state == answer_state.title()]
    if not correct_state.empty:
        coor = (float(correct_state.x), float(correct_state.y))
        write_state(str(correct_state.state.values[0]), coor, timmy)
        guessed_state.append(answer_state)




# # get mouse coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

screen.exitonclick()