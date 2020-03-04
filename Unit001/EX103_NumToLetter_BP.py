Temp = "零一二三四五六七八九"

i = input()

for j in i:
    print(Temp[eval(j)], end='') #该案例没能自己想出，对eval()、print()的理解不足。
