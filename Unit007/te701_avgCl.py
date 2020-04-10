#te701_avgCl.py
f = open("latex.log")
txt = f.readlines()
c = 0
l = 0
for i in txt:
    i = i.strip("\n")   #必须加，否则下面判断空值时，空行不能被正常识别，而是认为有\n
    if i != "":
        c += 1
        l += len(i)
print(round(l / c))