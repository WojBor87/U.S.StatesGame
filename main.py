import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_answer = []
life = 3


def write_state(state, color):
    x_cor = int(data[data["state"] == state].x)
    y_cor = int(data[data["state"] == state].y)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color(color)
    pen.setposition(x_cor, y_cor)
    pen.write(state)


while life:
    answer = turtle.textinput(title=f"{len(correct_answer)}/50 States Correct", prompt="What's another state name?").title()
    all_states = data["state"]
    if answer in all_states.tolist():
        if answer not in correct_answer:
            correct_answer.append(answer)
            write_state(answer, "black")
    else:
        life -= 1

missing_states = [write_state(state, "red") for state in data.state if state not in correct_answer]

turtle.mainloop()
