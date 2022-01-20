"""
创建两个线程，其中一个输出1-52，另外一个输出A-Z。
输出格式要求：
12A
34B
56C
...
5152Z
"""
# 思考：如何实现数字字母交替打印


import threading

lock1 = threading.Lock()  # 打印数字的锁
lock2 = threading.Lock()  # 打印字母的锁


def func1():  # 输出数字
    for i in range(1, 52, 2):
        lock2.acquire()
        print(f"{i}{i + 1}", end="")
        lock1.release()


def func2():  # 输出字母
    for i in range(65, 91):
        lock1.acquire()
        print(chr(i))
        lock2.release()


if __name__ == '__main__':
    # 创建两个线程对象
    process1 = threading.Thread(target=func1)
    process2 = threading.Thread(target=func2)
    # 对数字锁加锁, 即两个线程中,访问lock2的可以执行,访问 lock1 不能执行
    lock1.acquire()   # 保证先输出数字，lock1解锁，此时lock2已上锁，程序继续执行，找lock2解锁
    process1.start()
    process2.start()
