#503_KochDrawV0.py
import turtle
def curve(n):
    if n == 0:
        turtle.fd(1)
    else:
        curve(n-1)
        turtle.lt(60)
        curve(n-1)
        turtle.rt(120)
        curve(n-1)
        turtle.lt(60)
        curve(n-1)
curve(7)
