#ex702_countCha_BP.py
f = open("latex.log")
cc = 0
d = {}
for i in range(26): #构建字典，前26个为小写的26个英文字母。
    d[chr(ord('a')+i)] = 0
for line in f:  #求f中每个字符（包括大写及标点符号）的个数
    for c in line:
        d[c] = d.get(c, 0) + 1
        cc += 1
print("共{}字符".format(cc), end="")
for i in range(26):
    if d[chr(ord('a')+i)] != 0: #判断小写字符数量是否为0
        print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")
