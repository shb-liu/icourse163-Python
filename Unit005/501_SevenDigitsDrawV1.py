#501_SevenDigitsDrawV1.py
import turtle as t
def drawLine(draw):
    t.pd() if draw else t.pu()
    t.fd(40)
    t.rt(90)
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    t.lt(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.rt(180)
    t.pu()
    t.fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i)) #此处注意要用eval使i变为数字
def main():
    t.hideturtle()
    t.setup(800, 350, 200, 200)
    t.pu()
    t.fd(-300)
    t.pensize(5)
    drawDate('20200321')
    t.done()
main()
