f = open("latex.log")
ls = f.readlines()  #每行为元素的列表
s = set(ls) #所有行的集合
for i in s:
    ls.remove(i)    #ls列表中每个元素去除一次，即剩多次的数量
t = set(ls) #有重复数量的行的集合

print("共{}独特行".format(len(s)-len(t)))