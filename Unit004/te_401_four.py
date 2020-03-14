#te_401_four.py
for i in range(1000, 10000):
    s = 0
    for c in str(i):
        s += pow(eval(c), 4)
    if s == i:
        print(i)