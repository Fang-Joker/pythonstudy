from urllib import request, parse

'''
掌握对url进行参数编码的方法
需要使用parse模块
对get所用的参数进行编码，才能用get成功访问
'''

if __name__ == '__main__':

    url = 'http://www.baidu.com/s?'
    # 要向网页提供的数据参数
    wd = input("Input your keyword:")

    # 要想使用data， 需要使用字典结构
    qs = {
        "wd": wd
    }

    # 转换url编码，网页只认识编码，不认识直接输入的文字
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 如果直接用可读的带参数的url，是不能访问的
    #fullurl = 'http://www.baidu.com/s?wd=大熊猫'
    rsp = request.urlopen(fullurl)
    html = rsp.read()

    # 使用get取值保证不会出错
    html = html.decode()
    print(html)