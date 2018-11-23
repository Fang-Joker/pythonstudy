import multiprocessing
from time import ctime

# 设置哨兵问题
def consumer(input_q):
    print("Into consumer:", ctime())

    while True:
        item = input_q.get()
        # 这里解决了一个工作者不结束陷入死循环的问题，但是如果有
        # 多个子进程工作，原来给的一个哨兵信息就不够用了，要改进
        if item is None:
            break
        print("pull", item, "out of q")

    print ("Out of consumer:", ctime()) ## 此句执行完成，再转入主进程

def producer(sequence, output_q):
    print ("Into procuder:", ctime())

    for item in sequence:
        output_q.put(item)
        print ("put", item, "into q")

    print ("Out of procuder:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue() # 依靠队列通知消息
    cons_p = multiprocessing.Process(target = consumer, args = (q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    # 对多个子进程，可以预先防止多个重复的哨兵信息
    q.put(None)
    q.put(None)
    cons_p.join()