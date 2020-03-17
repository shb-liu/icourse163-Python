#spd004_ng_ng_pix_v1.py
import requests
import os
url = 'http://image.ngchina.com.cn/2020/0316/20200316124042110.jpg'
root = '/Users/user/Desktop/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
