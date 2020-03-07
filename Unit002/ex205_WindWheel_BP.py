#ex205_WindWheel_BP.py
import turtle as t
t.width(2)
for i in range (4):
    t.seth(90*i)
    t.fd(150)
    t.rt(90)
    t.circle(-150, 45)
    t.goto(0, 0)
t.done()