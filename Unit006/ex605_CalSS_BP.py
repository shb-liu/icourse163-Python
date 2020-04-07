import jieba
f = open("沉默的羔羊.txt")
ls = jieba.lcut(f.read())   #变为列表
#ls = f.read().split()
d = {}
for w in ls:    #构建字典d，key为单词，value为次数。
    d[w] = d.get(w, 0) + 1
maxc = 0
maxw = ""
for k in d: #逐一对比key
    if d[k] > maxc and len(k) > 2:  #字典d的key值，即词数量大于上一个词的数量，且key长度大于2
        maxc = d[k]
        maxw = k
    if d[k] == maxc and len(k) > 2 and k > maxw:
        #字典d的key值，即词数量等于上一个词的数量，且key大于上一个词的值，unicode
        maxw = k
print(maxw)
f.close()