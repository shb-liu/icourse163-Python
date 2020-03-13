#403_CalPiv1.py
pi = 0
n = 100
for i in range (n):
    pi += 1/pow(16, i)*( \
        4/(8*i+1) - 2/(8*i+4) - \
        1/(8*i+5) - 1/(8*i+6))
print("圆周率值是：{}".format(pi))