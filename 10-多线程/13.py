#
import threading
import time

import queue

# 模拟生产者的类,继承自线程
class Producer(threading.Thread):

    def run(self): # 必须重写run，真正干活的函数
        global queue
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count +1
                    msg = '生成产品'+str(count)
                    # put是网queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):

    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg = self.name + '消费了 '+queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))

    for i in range(2):
        p = Producer() # 实例化生产者线程
        p.start()

    for i in range(5):
        c = Consumer() # 实例化消费者线程
        c.start()
    # 接下来就随他们跑了