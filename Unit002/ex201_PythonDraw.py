#ex201_PythonDraw.py
import turtle as t
t.setup(800, 600)
t.pu()
t.bk(300)
t.pd()
t.width(25)
t.color('purple')
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 40)
t.fd(30)
t.circle(15, 180)
t.fd(20)
t.done()