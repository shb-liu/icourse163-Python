#spd003_baidu_python.py
import requests
keyword = 'python'
try:
    kv = {'wd': keyword}
    r = requests.get('https://www.baidu.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print("error")