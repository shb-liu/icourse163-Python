#ex_403_intSum.py
s = 0
for i in range(1, 966+1):
    if i % 2 == 0:
        s -= i
    else:
        s += i
print("{}".format(s))