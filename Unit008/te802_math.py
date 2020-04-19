#te802_math.py
a = input()
try:
    if complex(a) == complex(eval(a)):
        print(eval(a) ** 2)
except:
    print("输入有误")