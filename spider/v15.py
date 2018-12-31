
from urllib import request, parse
from http import cookiejar

#  创建filecookiejar的实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

# 生成 cookie的管理器实例
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器，包含以上三个管理器
# 之后就可以用opener实例管理获取cookie了
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''

    # 此url需要从登录页面form标签的action属性中提取
    # 该URL是登陆时实际访问的链接
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登录form的两个对应input中提取name属性
    # 从源码查找实际账号和密码对应的name属性
    data = {
        "email": "13119144223",
        "password": "123456"
    }

    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求（不是直接访问页面），从对象中自动获取cookie
    rsp = opener.open(req)
    # 保存cookie到文件,参数分别为忽略丢弃和忽略过期
    cookie.save(ignore_discard = True, ignore_expires = True)

if __name__ == '__main__':
    login()
