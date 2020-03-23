#ex_503_cmul.py
# 请在...补充一行或多行代码
def cmul(*b):
    a = 1
    for i in b:
        a *= i
    return a
print(eval("cmul({})".format(input())))