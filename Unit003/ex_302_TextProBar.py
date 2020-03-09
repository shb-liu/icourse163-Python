#ex_302_TextProBar.py
import time as t
step = 50
print("执行开始".center(30, '-'))
start = t.perf_counter()
for i in range (step + 1):
    a = '*' * i
    b = '.' * (step - i)
    c = i / step * 100
    dur = t.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    t.sleep(0.1)
print('\n'+"执行结束".center(30, '-'))