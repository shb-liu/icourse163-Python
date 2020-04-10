#ex703_uniqL.py
a = open("latex.log")
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
c = 0
for i in d:
    if d[i] == 1:
        c += 1
    else:
        continue
print("共{}独特行".format(c))