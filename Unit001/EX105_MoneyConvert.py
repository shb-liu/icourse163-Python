#MoneyConvert.py
m = input()
if m[0:3] in ['USD']:
    rmb = eval(m[3:]) * 6.78
    print('RMB{:.2f}'.format(rmb))
elif m[0:3] in ['RMB']:
    usd = eval(m[3:]) / 6.78
    print('USD{:.2f}'.format(usd))
else:
    print()