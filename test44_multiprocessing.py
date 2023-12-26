# @time     ：2023/12/26 14:23
# @author   : 莉光哈哈哈
# @file     : test44_multiprocessing.py
# @software : PyCharm
'''
创建和运行进程
    使用multiprocessing.Process()来创建一个进程。有两个重要的参数：
        target：一个可调用对象（函数），这个进程将在进程启动时被调用
        args：函数参数，元组
'''
# from multiprocessing import Process
# import os
#
#
# def square_numbers():
#     for i in range(1000):
#         result = i * i
#
#
# if __name__ == '__main__':
#     processes = []
#
#     num_processes = os.cpu_count()
#     print(num_processes)  # 计算机中的CPU数量
#
#     # 构造多个进程
#     for _ in range(num_processes):
#         process = Process(target=square_numbers())
#         processes.append(process)
#
#     # 执行进程，等待进程结束
#     for process in processes:
#         process.start()
#         process.join()

'''
在进程间共享数据
    数据可以通过Value或者Array来存储在共享内存中
        Value(type,value):创建一个ctypes对象的类型是type。访问值是.target
        Array(type,value):创建一个ctypes数组，其元素的类型是type。访问值使用[]
'''
# from multiprocessing import Process, Value, Array
# import time
#
#
# # 增加100次
# def add_100(number):
#     for _ in range(100):
#         time.sleep(0.01)
#         number.value += 1
#
#
# # number中每个位置增加100次
# def add_100_array(numbers):
#     for _ in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             numbers[i] += 1


# if __name__ == '__main__':
#     shared_number = Value("i", 0)
#     print('Value at beginning:', shared_number.value)
#     shared_array = Array("d", [0.0, 100.0, 200.0])
#     print("Array at beginning:", shared_array[:])
#
#     process1 = Process(target=add_100, args=(shared_number,))
#     process2 = Process(target=add_100, args=(shared_number,))
#     process3 = Process(target=add_100_array, args=(shared_array,))
#     process4 = Process(target=add_100_array, args=(shared_array,))
#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()
#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()
#     print("Value at end:", shared_number.value)
#     print("Array at end:", shared_array[:])
#     print("end main")

'''
通过锁来解决竞争条件
    Lock有两种状态：locked和unlocked
        lock.acquire():这将锁定状态并阻塞
        lock.release():这将再次解锁状态
'''
# from multiprocessing import Lock
# from multiprocessing import Process, Value, Array
# import time
#
#
# def add_100(number, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         lock.acquire()  # 上锁
#         number.value += 1
#         lock.release()  # 解锁
#
#
# def add_100_array(numbers, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             lock.acquire()  # 上锁
#             numbers[i] += 1
#             lock.release()  # 解锁


# if __name__ == '__main__':
#     lock = Lock()
#     shared_number = Value('i', 0)
#     print("Value at beginning:", shared_number.value)
#     shared_array = Array('d', [0.0, 100.0, 200.0])
#     print("Array at beginning:", shared_array[:])
#
#     # 锁定共享资源
#     process1 = Process(target=add_100, args=(shared_number, lock))
#     process2 = Process(target=add_100, args=(shared_number, lock))
#     process3 = Process(target=add_100_array, args=(shared_array, lock))
#     process4 = Process(target=add_100_array, args=(shared_array, lock))
#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()
#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()
#     print("Value at end:", shared_number.value)
#     print("Array at end:", shared_array[:])
#     print("end main")

'''
通过队列来使用进程
    队列遵循先进先出（FIFO）原则的线性数据结构
'''
# from multiprocessing import Queue
#
# q = Queue()  # 创建一个队列
# # 增加一个元素
# q.put(1)
# q.put(2)
# q.put(3)
# # 后---》3，2，1《---前
# # 取出元素会是最前面的
# first = q.get()
# print(first)


'''
在多进程中使用队列
    重要的方法是：
        q.get()：删除并返回第一列，默认情况下，它会阻塞，直到该项目可用
        q.put(item)：将元素放在队列的末尾，默认情况下，它会阻塞，直到有空闲插槽可用
        q.empty()：如果队列为空，则返回True
        q.close()：表示当前进程不会再将数据放入此队列
'''
# from multiprocessing import Process, Queue
#
#
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i * i)
#
#
# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(i * -1)
#
#
# if __name__ == '__main__':
#     numbers = range(1, 6)
#     q = Queue()
#     p1 = Process(target=square, args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     while not q.empty():
#         print(q.get())
#     print("end main")


'''
进程池
    map(func, iterable[, chunksize]) ：此方法将可迭代对象分割成若干块，作为单独的任务提交给进程池。这些块的（近似）大小可以通过将 chunksize 设置为正整数来指定。它阻塞，直到结果准备好。
    close() : 防止任何更多的任务被提交到池中。完成所有任务后，工作进程将退出。
    join()：等待工作进程退出。在使用 join() 之前必须调用 close() 或 terminate()。
    apply(func, args)：使用参数 args 调用 func。它阻塞，直到结果准备好。 func 仅在池的一个工人中执行。
'''

from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == '__main__':
    numbers = range(10)
    p = Pool()
    result = p.map(cube, numbers)
    p.close()
    p.join()
    print(result)
