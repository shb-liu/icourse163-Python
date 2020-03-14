#te_402_sh.py
from math import ceil
a = eval(input())
for i in range(2, ceil(pow(a, 0.5)) +1):
    if a % i ==0:
        break
else:
    print(a)