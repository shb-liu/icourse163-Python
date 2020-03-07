#PythonDraw_fi.py
from turtle import *
setup(650, 350, 200, 200)
pu()
fd(-250)
pd()
width(25)
pencolor('purple')
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)
circle(16, 180)
fd(40 * 2/3)
done()