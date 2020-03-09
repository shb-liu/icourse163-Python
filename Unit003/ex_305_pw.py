#ex_305_pw.py
t = input()
p = ''
for i in t:
    if 'a' <= i <= 'z': #可以直接使用字符进行比较，即比较字符的Unicode，ord()的值。
        p += chr((ord(i) - ord('a') + 3) % 26 + ord('a'))
    elif 'A' <= i <= 'Z':
        p += chr((ord(i) - ord('A') + 3) % 26 + ord('A'))
    else:
        p += i
print(p)