#ex_502_koch.py
# 请在...补充一行或多行代码
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for i in [0, 60, -120, 60]:
            turtle.lt(i)
            koch(size / 3, n-1)
def main(level):
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    size = 400
    for i in range(3):
        koch(size, level)
        turtle.right(120)
try:
    level = eval(input("请输入科赫曲线的阶: "))
    main(level)
except:
    print("输入错误")