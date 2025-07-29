from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_counterclockwise():
    tim.left(10)
def turn_clockwise():
    tim.right(10)
def clear_screen():
    tim.clear()
    move_to_start()
def move_to_start():
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setposition(0,0)
    tim.setheading(0)
    tim.showturtle()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)
#screen.onkey(key="c", fun=move_to_start)

screen.exitonclick()
