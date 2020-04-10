#ex702_countCha.py
a = open("latex.log", "r").read().replace("\n","")
t = ""
s = 0
for i in "abcdefghijklmnopqrstuvwxyz":
    c = 0
    for j in a:
        if j == i:
            c += 1
    s += c
    t += ",{}:{}".format(i, c)
print("共{}字符{}".format(s, t))
#未包含非小写字母的字符数量，以及跳过个数为0的数