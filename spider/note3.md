# 动态HTML
- dhtml
## 爬虫跟反爬虫
### 动态HTML介绍
- JavaScrapt（将功能推到前端，比较完善的语言）
- jQuery（前端一般都要用）
- Ajax（数据可以不放在网页上，而通过ajax异步请求数据，也是爬虫要跳过的部分）
- DHTML

- Python采集动态数据 
    - 从Javascript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面
## Selenium + PhantomJS
- Selenium: web自动化测试工具，自动操纵浏览器 
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装： pip install selenium==2.48.0
    - 官网： http://selenium-python.readthedocs.io/index.html

- PhantomJS(幽灵) 
    - 基于Webkit 的无界面的浏览器，由Selenium操纵
    - 官网： http://phantomjs.org/download.html
- Selenium 库有有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例 v37
- chrome + chromedriver 
    - 下载安装chrome： 下载+安装
    - 下载安装chromedriver：并且配置环境路径
- Selenium操作主要分两大类： 
    - 得到UI元素 
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟 
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
        - 案例38
- 用浏览器爬非常消耗资源，一般进行大量爬取使用浏览器不合适