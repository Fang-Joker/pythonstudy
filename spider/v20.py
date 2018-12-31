'''
爬取豆瓣电影数据
了解ajax的基本爬去方式
ajax返回的是json格式
'''
'''
https://movie.douban.com/j/chart/top_list?
type=11&     # 类型编号
interval_id=100%3A90&   # 区间标志
action=      # 
&start=40    # 开始的序号
&limit=20    # 每次访问出现的最多数量
'''
from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=60&limit=20"

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)

