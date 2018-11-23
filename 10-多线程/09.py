import threading
import time

# 1. 类需要继承自threading.Thread
class MyThread(threading.Thread):

    # 要写构造函数的话最好直接使用父类构造函数
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 2 必须重写run函数，run函数代表的是真正执行的功能
    # 相当于写了个自己想要的执行内容的子线程，只能执行run里的
    def  run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("Main thread is done!!!!!!!!")