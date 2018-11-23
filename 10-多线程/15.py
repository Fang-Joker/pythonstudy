import threading
import time

# 锁的等待时间，一旦等了一段时间未获得，就直接往下走
# 这个程序知识暂时解决死锁问题
lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
   print("func_1 starting.........")
   # 设置等待时间，超出就释放所有锁
   lock_1.acquire(timeout=4)
   print("func_1 申请了 lock_1....")
   time.sleep(2)
   print("func_1 等待 lock_2.......")

   rst = lock_2.acquire(timeout=2)
   if rst:
       print("func_1 已经得到锁 lock_2")
       lock_2.release()
       print("func_1 已经释放锁 lock_2")
   else:
       print("func_1 没得到锁 lock_2")

   lock_1.release() # 这里其实会出问题，因为不能保证能申请到锁1
   print("func_1 释放了 lock_1")

   print("func_1 done..........")

def func_2():

   print("func_2 starting.........")
   lock_2.acquire()
   print("func_2 申请了 lock_2....")
   time.sleep(4)
   print("func_2 等待 lock_1.......")

   lock_1.acquire()
   print("func_2 申请了 lock_1.......")
   lock_1.release()
   print("func_2 释放了 lock_1")

   lock_2.release()
   print("func_2 释放了 lock_2")

   print("func_2 done..........")



if __name__ == "__main__":
   print("主程序启动..............")

   t1 = threading.Thread(target=func_1, args=())
   t2 = threading.Thread(target=func_2, args=())

   t1.start()
   t2.start()

   t1.join()
   t2.join()

   print("主程序启动..............")