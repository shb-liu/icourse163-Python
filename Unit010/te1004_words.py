#te1004_words.py
import jieba
txt = open("沉默的羔羊.txt").read()
b = jieba.lcut(txt)
c = {}
for i in b:
    if len(i) > 2:
        c[i] = c.get(i,0) + 1
    else:
        continue
n = 0
r = ""
for i in c:
    if c[i] > n:
        n = c[i]
        r = i
print(r)