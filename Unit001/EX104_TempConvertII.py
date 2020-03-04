#TempConvertII.py
Temp = input()
if Temp[0] in ['F', 'f']:
    C = (eval(Temp[1:]) - 32)/1.8
    print('C{:.2f}'.format(C))
else:# Temp[0] in ['C', 'c']:
    F = eval(Temp[1:]) * 1.8 + 32
    print('F{:.2f}'.format(F))