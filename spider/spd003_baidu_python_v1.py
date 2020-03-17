#spd003_baidu_python_v1.py
import requests
keyword = 'python'
try:
    kvh = {}
    kvh[
        'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'  # http头大小写不敏感
    kvh['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    kvh['Connection'] = 'keep-alive'
    kvh['Upgrade-Insecure-Requests'] = '1'
    kv = {'wd':keyword}
    r = requests.get('https://www.baidu.com/s',headers=kvh, params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print("error")