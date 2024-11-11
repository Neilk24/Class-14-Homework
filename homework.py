import turtle
import time

turtle.Screen().bgcolor("aqua")
board=turtle.Turtle()
n=3

while n>=0:
    board.forward(100)
    board.right(90)
    n=n-1

time.sleep(5)

turtle.done