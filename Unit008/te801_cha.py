#te801_cha.py
a = input()
b = "abcdefghijklmnopqrstuvwxyz"
c = ""
for i in a:
    if i in b:
        c += i
print(c)