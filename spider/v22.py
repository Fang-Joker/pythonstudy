'''
使用参数headers和params
研究返回结果
'''

import requests

# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"

kw = {
    "wd": "王八蛋"
}
# 实际使用要尽可能伪装
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

rsp = requests.get(url, params=kw, headers=headers )

print(rsp.text)
print()
print(rsp.content)
print()
print(rsp.url)
print()
print(rsp.encoding)
print()
print(rsp.status_code) # 请求返回码