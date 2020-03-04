#TempConvertII.py
Temp = input()
if Temp[0] in ['F', 'f']:
    C = (eval(Temp[1:]) - 32)/1.8
    print('C{:.2f}'.format(C))
else:# Temp[0] in ['C', 'c']:
    F = eval(Temp[1:]) * 1.8 + 32
    print('F{:.2f}'.format(F))
#该案例老师使用了if，elif，else来编写程序。因为原题规定假定不存在错误输入，因此采用该方法。