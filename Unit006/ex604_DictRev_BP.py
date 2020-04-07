#ex604_DictRev_BP.py
#未能想到解决方案。
s = input() #输入字典赋值到s，但格式为str
try:
    d = eval(s) #将s转为字典
    e = {}
    for k in d:
        e[d[k]] = k #字典e的key即为d[k]=>字典d中k对应的值，而e的值为k，即d中的键
    print(e)
except:
    print("输入错误")