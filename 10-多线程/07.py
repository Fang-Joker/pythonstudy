# 守护线程
# 子线程生命同主线程

import time
import threading

def fun():

    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
# 要先将线程设置为守护线程再启动才有效
t1.setDaemon(True)
t1.start()

# 设置主线程睡1s，子线程睡2s，主线程结束后，子线程也跟着直接结束
# 打印其中的内容
time.sleep(1)
print("Main thread end")