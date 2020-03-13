#ex_404_three.py
p = ""
for i in range(100, 1000):
    s = 0
    for c in str(i):
        s += pow(eval(c), 3)
    if s == i:
        #print("{}".format(i), end=',') #会多一个逗号
        p += "{},".format(i) #将符合的数字变为字符圈的集合，此时也多逗号
print(p[:-1])#此处去掉逗号打印