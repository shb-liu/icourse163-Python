#spd001_JD_ikbc.py
import requests
url = "https://item.jd.com/100006367852.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("获取失败")