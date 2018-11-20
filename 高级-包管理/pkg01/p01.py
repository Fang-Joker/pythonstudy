
# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():

    def __init__(self, name = "NoName", age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("Hi, come here!")

# 使用请看p02
# 本身进行测试，而避免在被调用时直接执行
# 当文件本身被作为主进程使用（即自己执行）时，
# 主进程的名字就是main
# 当其被调用时，就不会执行，因为此时这个文档不是主进程
# 此判断语句建议一直作为程序的入口，执行起点，好习惯
if __name__ == '__main__':
    print("这个文档自己本身的使用")