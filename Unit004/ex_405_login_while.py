#ex_405_login_while.py
i = 0
while i < 3:
    u = input()
    p = input()
    if u == "Kate" and p == "666666":
        print("登录成功！")
        break
    else:
        i += 1
else:
    print("3次用户名或者密码均有误！退出程序。")