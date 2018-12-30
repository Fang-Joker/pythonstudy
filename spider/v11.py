from urllib import request

# 没有cookie时，即使使用别人已经登入的链接依旧不能进入，服务器匹配不到访问信息
if __name__ == '__main__':

    url = "http://www.renren.com/965187997/profile"

    rsp = request.urlopen(url)
    html = rsp.read().decode()

    with open("rsp.html", "w") as f:

        f.write(html)