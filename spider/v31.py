from lxml import etree

# 只能读取xml格式内容，html报错,
# 该函数处理为相应的etree元素树，方便进一步使用方法
html = etree.parse("./v30.html")
print(type(html))

rst = etree.tostring(html, pretty_print=True)
print(rst)