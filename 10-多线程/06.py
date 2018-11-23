# 非守护线程
# 子线程基本与主线程平行

import time
import threading

def fun():

    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
t1.start()

# 设置主线程睡1s，子线程睡2s，主线程结束后，子线程依旧执行
# 打印其中的内容
time.sleep(1)
print("Main thread end")