#spd002_amazon_cherry_v1.py
import requests
url = 'https://www.amazon.cn/dp/B000JWEI3O'
try:
    kv = {}
    kv[
        'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'  # http头大小写不敏感
    kv['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    kv['Connection'] = 'keep-alive'
    kv['Upgrade-Insecure-Requests'] = '1'
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[2000:3000])
except:
    print("读取有误")