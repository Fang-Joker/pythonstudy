# 正常情况下，是无法导入以数字开头的包的，但是可以
# 借助importlib库就可以
import importlib

# 相当于importlab导入了一个名为01的模块并赋给了tuling
# 之后正常使用tuling即可
tuling = importlib.import_module("01")

stu = tuling.Student("asd", 23)
stu.say()
tuling.sayHello()