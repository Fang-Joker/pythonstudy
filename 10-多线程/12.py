# 使用锁保护可能被共用的变量
# 此时，结果正确

import threading

sum = 0
loopSum = 1000000

# 实例化一把锁
lock = threading.Lock()

def myAdd():
    global sum, loopSum

    for i in range(1, loopSum):
        # 对要加锁的操作加锁
        lock.acquire()
        sum += 1
        # 使用完释放锁
        lock.release()

def myMinu():
    global sum, loopSum

    for i in range(1, loopSum):
        # 对要加锁的操作加锁
        lock.acquire()
        sum -= 1
        # 使用完释放锁
        lock.release()

if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))