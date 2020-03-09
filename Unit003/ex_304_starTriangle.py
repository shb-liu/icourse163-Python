#ex_304_starTriangle.py
"""t = eval(input()) // 2
l = t * 2 + 1
for i in range(t + 1):
    print('{:^{}}'.format(((2 * i + 1) * '*'), l))"""

t = eval(input())
for i in range(1, t+1, 2):  #range()可以有三个参数（开始点，结束点，步长）
    print('{:^{}}'.format((i * '*'), t))