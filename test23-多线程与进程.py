# 时间：2023/6/10 11:09
# 人员: 莉光哈哈哈

import _thread
import logging
import threading
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)

#第一种
# def loop1():
#     logging.info("start loop1 at"+ctime())
#     sleep(4)
#     logging.info("end loop1 at"+ctime())
#
# def loop2():
#     logging.info("start loop2 at"+ctime())
#     sleep(2)
#     logging.info("end loop2 at"+ctime())
# def main():
#     logging.info("start all at"+ctime())
#     _thread.start_new_thread(loop1,())
#     _thread.start_new_thread(loop2,())
#     sleep(6)
#     logging.info("end all at"+ctime())
# if __name__ == "__main__":
#     main()

#第二种
# loops=[2,4]
# def loop(nloop,nsec,lock):
#     logging.info("start loop"+str(nloop)+"at"+ctime())
#     sleep(nsec)
#     logging.info("end loop"+str(nloop)+"at"+ctime())
#     lock.release()
# def main():
#     logging.info("start all at"+ctime())
#     locks=[]
#     nloops=range(len(loops))
#     for i in nloops:
#         lock=_thread.allocate_lock()
#         lock.acquire()#加锁操作
#         locks.append(lock)
#     for i in nloops:
#         _thread.start_new_thread(loop,(i,loops[i],locks[i]))
#     for i in nloops:
#         while locks[i].locked():
#             pass
#     logging.info("end all at"+ctime())
# if __name__ == "__main__":
#     main()

loops=[2,4]

class MyThread(threading.Thread):
    def __int__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop "+str(nloop)+" at"+ctime())
    sleep(nsec)
    logging.info("end loop "+str(nloop)+" at"+ctime())

# def threading(loop,param):
#     pass

def main():
    logging.info("start all at"+ctime())
    threads=[]
    nloops=range(len(loops))
    for i in nloops:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        # t=MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at"+ctime())
if __name__ == "__main__":
    main()