#ex_503_fbi.py
# 请在...补充一行或多行代码
def fbi(n):
#    if n == 1:
#        return  1
#    elif n == 2:
#        return  1
    if n == 1 or n == 2:
        return 1
    else:
#        a = fbi(n-1) + fbi(n-2)
#        return a
        return fbi(n-1) + fbi(n-2)
n = eval(input())
print(fbi(n))