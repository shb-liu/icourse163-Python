#802_BatchInstall.py
import os
libs = {"numpy", "matplotlib", "pillow", "wheel", "django", "flask"}
try:
    for lib in libs:
        os.system("pip3 install " + lib)
    print("安装成功")
except:
    print("安装失败")