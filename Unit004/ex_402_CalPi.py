#ex_402_calPi.py
import random as r
p = 0
n = eval(input())
h = 0
r.seed(123)
for i in range(n):
    x, y = r.random(), r.random()
    if pow(x ** 2 + y ** 2, 0.5) <= 1:
        h += 1
p = h/n*4
print("{:.6f}".format(p))