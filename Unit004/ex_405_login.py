#ex_405_login.py
for i in range(3):
    u = input()
    p = input()
    if u == "Kate" and p == "666666": #此处应用and判断
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")