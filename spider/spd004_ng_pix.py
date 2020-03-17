#spd004_ng_pix.py
import requests
path = '/Users/user/Desktop/123.jpg'
url = 'http://image.ngchina.com.cn/2020/0316/20200316124042110.jpg'
r = requests.get(url)
with open(path, 'wb') as f:
    f.write(r.content)
    f.close()
    print('文件保存成功')