#503_KochDrawV1.py
import turtle
def koch(size, n):
    if n == 1:
        turtle.fd(size)
    else:
        for i in [0, 60, -120, 60]:
            turtle.lt(i)
            koch(size / 3, n-1)
def main():
    turtle.setup(800,400)
    turtle.pu()
    turtle.goto(-300, -50)
    turtle.pd()
    turtle.pensize(2)
    koch(600,3)
    turtle.hideturtle()
main()
