#te_501_genpwd.py
#补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，密码的每位是一个数字。每个密码单独一行输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#产生密码采用random.randint()函数。

##############个人解答
#import random
#def genpwd(length):
#    a = ""
#    for i in range(length):
#        a += str(random.randint(0,10))
#    return a
#length = eval(input())
#random.seed(17)
#for i in range(3):
#    print(genpwd(length))

import random
def genpwd(length):
    return random.randint(pow(10, length - 1), pow(10, length) - 1)
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))