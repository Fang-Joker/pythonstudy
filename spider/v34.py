from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')
print(soup.link) # 找到第一个link标签的所有内容
print(soup.link.attrs) # attrs是属性，以字典形式表达
print("==" * 12)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
# 由于全部读取进内存，可以以字典方式直接修改
print("==" * 12)
print(soup.name) # soup本身
print(soup.attrs)
print("==" * 12)
print("==" * 12)

# tags = soup.find_all(re.compile('^me'), content="always")
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node)

