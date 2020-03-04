n = eval(input())#n = input() 是后面if判断更加简单。
if n > 0:
    print('He\nll\no \nWo\nrl\nd') #此处可以写在一行。\n为换行符号。
elif n == 0:
    print('Hello World')
elif n < 0:
    for c in 'Hello World':
        print(c) #此处应使用for语句来换行。由于做EX103时没有实验print()函数中增加, end=""的作用，导致只能逐行输入。
else:
    print()