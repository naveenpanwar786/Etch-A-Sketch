from turtle import Turtle, Screen

tim = Turtle()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def antiClock():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()


screen = Screen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=antiClock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.listen()
screen.exitonclick()