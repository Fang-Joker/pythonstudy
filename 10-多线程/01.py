# 用time函数，生成两个函数
# 顺序调用,即模拟单线程执行的状况
# 计算总的调用时间

import time

def loop1():
    # ctime得到当前时间
    print('Start loop 1 at:', time.ctime())
    # 睡眠
    time.sleep(4)
    print('End loop 1 at :', time.ctime())

def loop2():
    # ctime得到当前时间
    print('Start loop 2 at:', time.ctime())
    # 睡眠
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

# 打印一条时间很短，主要在上面的睡眠
def main():
    print("Start at:", time.ctime())
    loop1()
    loop2()
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()