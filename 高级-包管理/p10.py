from pkg02 import *

# 此时便可以使用__init__.py文件中__all__设置的模块
# 此时其__init__内部的其他函数无效
stu = p01.Student() # 可以直接使用名字，因为*的缘故
stu.say()