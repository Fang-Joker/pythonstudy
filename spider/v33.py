from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

# lxml是解析引擎
soup = BeautifulSoup(content, 'lxml')
print(type(soup))
# bs自动转码，不需要手动解码
content = soup.prettify() # 该方法将bs4实例转化为字符串类型
print(type(content))
print(content)