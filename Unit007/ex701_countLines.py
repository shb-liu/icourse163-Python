#ex701_countLines.py
a = open("latex.log", "r").readlines()
c = 0
for i in a:
    if i != "\n":
        c += 1
print("共{}行".format(c))