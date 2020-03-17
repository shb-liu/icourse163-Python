#spd005_checkIP.py
import requests
url = 'https://www.ip138.com/iplookup.asp?ip='
ip = '202.204.80.112'
kvh = {}
kvh[
    'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'  # http头大小写不敏感
kvh['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
kvh['Connection'] = 'keep-alive'
kvh['Upgrade-Insecure-Requests'] = '1'
kv = {'action':'2'}
try:
    r = requests.get(url + ip, headers=kvh, params=kv)
    r.raise_for_status()
    print(r.request.url)
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('爬取失败')