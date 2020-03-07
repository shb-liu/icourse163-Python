#ex205_windwheel.py
import turtle as t
t.width(3)
for i in range(4):
    t.fd(150)
    t.rt(90)
    t.circle(-150, 45)
    t.rt(90)
    t.fd(150)
    t.rt(45)
t.done()