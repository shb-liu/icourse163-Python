#TempConvertII.py
T = input()
if T[0] in ['C']:
    F = eval(T[1:]) * 1.8 + 32
    print('F{:.2f}'.format(F))
elif T[0] in ['F']:
    C = (eval(T[1:]) - 32)/1.8
    print('C{:.2f}'.format(C))
else:
    print()