#ex701_countLines_BP.py
f = open("latex.log")
s = 0
for line in f:
    line = line.strip('\n')
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))