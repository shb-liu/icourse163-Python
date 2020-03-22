#503_KochDrawV2.py
import turtle
def koch(size, n):
    if n == 1:
        turtle.fd(size)
    else:
        for i in [0, 60, -120, 60]:
            turtle.lt(i)
            koch(size / 3, n-1)
def main():
    turtle.setup(600,600)
    turtle.pu()
    turtle.goto(-200, 100)
    turtle.pd()
    turtle.pensize(2)
    level = 3
    for i in range(level):
        koch(400, level)
        turtle.rt(120)
    turtle.hideturtle()
main()
