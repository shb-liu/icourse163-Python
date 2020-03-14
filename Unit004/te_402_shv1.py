#te_402_shv1.py
s = 0
for a in range(2, 1000):
    for i in range(2, round(pow(a, 0.5)) + 1):
        if a % i == 0:
            break
    else:
        s += a
        #print(a)
print(s)
