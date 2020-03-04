#TempConvert.py
Temp = input()
if Temp[-1] in ['F', 'f']:
    C = (eval(Temp[0:-1]) - 32)/1.8
    print('{:.2f}C'.format(C))
elif Temp[-1] in ['C', 'c']:
    F = eval(Temp[0:-1]) * 1.8 + 32
    print('{:.2f}F'.format(F))
else:
    print('输入格式错误。')