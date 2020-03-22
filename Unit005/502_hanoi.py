#503_hanoi.py
count = 0   #用来计数，一共需要多少步
def hanoi(i, src, dst, mid):
    global count
    if i == 1:
        print("{}:{}=>{}".format(1, src, dst))
        count += 1
    else:   #只考虑第n次与第n-1的关系。即用第n-1计算的结果来计算第n次的运算境况。
        hanoi(i-1, src, mid, dst)
        print("{}:{}=>{}".format(i, src, dst))
        hanoi(i-1, mid, dst, src)
        count += 1
hanoi(5, 'a', 'b', 'c')
print(count)