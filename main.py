from turtle import Turtle, Screen

foli = Turtle()
screen = Screen()


def move_forwards():
    foli.forward(10)


def move_backwards():
    foli.backward(10)


def rotate_right():
    foli.right(10)


def rotate_left():
    foli.left(10)


def clear():
    foli.clear()
    foli.penup()
    foli.home()
    foli.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
