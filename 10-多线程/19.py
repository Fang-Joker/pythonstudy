# 多进程包
import multiprocessing
from time import sleep, ctime

def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target = clock, args = (5,))
    p.start()

    # 主进程死掉了，这里子进程也死了，保持主进程一直进行
    while True:
        print('sleeping.......')
        sleep(1)