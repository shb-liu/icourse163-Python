#ex_501_SevenDigitsDraw.py
import turtle
import time
def drawGap():
    turtle.pu()
    turtle.fd(3)
def drawLine(draw):
    drawGap()
    turtle.pd() if draw else turtle.pu()
    turtle.fd(30)
    drawGap()
    turtle.rt(90)
def drawDigits(digit):
    for i in digit:
        drawLine(True) if i in ['2', '3', '4', '5', '6', '8', '9', 'A', 'B', 'D', 'E', 'F'] else drawLine(False)
        drawLine(True) if i in ['0', '1', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'D'] else drawLine(False)
        drawLine(True) if i in ['0', '2', '3', '5', '6', '8', '9', 'B', 'C', 'D', 'E'] else drawLine(False)
        drawLine(True) if i in ['0', '2', '6', '8', 'A', 'B', 'C', 'D', 'E', 'F'] else drawLine(False)
        turtle.lt(90)
        drawLine(True) if i in ['0', '4', '5', '6', '8', '9', 'A', 'B', 'C', 'E', 'F'] else drawLine(False)
        drawLine(True) if i in ['0', '2', '3', '5', '6', '7', '8', '9', 'A', 'C', 'E', 'F'] else drawLine(False)
        drawLine(True) if i in ['0', '1', '2', '3', '4', '7', '8', '9', 'A', 'D'] else drawLine(False)
        turtle.lt(180)
        turtle.pu()
        turtle.fd(10)
def main():
    turtle.setup(1000, 150)
    turtle.speed(0)
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.pu()
    turtle.goto(-450,0)
    #drawDigits('0123456789ABCDEF')
    drawDigits(time.strftime('%Y%m%d'.format(time.localtime())))
    turtle.done()
main()