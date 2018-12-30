from urllib import request

# 将cookie放入请求头，访问该链接
if __name__ == '__main__':

    url = "http://space.bilibili.com/4238585?"

    headers = {
        "Cookie": 'bsource=seo_baidu; buvid3=B53881EC-C41A-402D-99C7-250EDECEE92D85545infoc; LIVE_BUVID=AUTO1615461763988712; sid=98d5jxg1; DedeUserID=4238585; DedeUserID__ckMd5=7d4d99a9d0ce2ff0; SESSDATA=5a499651%2C1548768420%2C4b3aaec1; bili_jct=6b3a2a045b0b0992d67b558dfd61586e; _dfcaptcha=48c9107c062a6ecd59286ac279548b3a; _uuid=D55312C0-135A-F6EA-9D1A-486DC982201705133infoc'
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode('UTF-8')
    # print(html)
    with open("rsp3.html", "w", encoding="UTF-8") as f:

        f.write(html)