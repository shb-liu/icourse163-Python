CurStr = input()
if CurStr[:3] == "RMB":
    print("USD{:.2f}".format(eval(CurStr[3:])/6.78))#可以直接将公式写在format内。
elif CurStr[:3] in ['USD']:
    print("RMB{:.2f}".format(eval(CurStr[3:])*6.78))