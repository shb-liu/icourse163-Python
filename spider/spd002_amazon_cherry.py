#spd002_amazon_cherry.py
import requests
url = 'https://www.amazon.cn/dp/B000JWEI3O'
try:
    kv = {'uaer-agent':'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[2000:3000])
except:
    print("获取出错")