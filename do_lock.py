#!/usr/bin/env python
# encoding: utf-8
import time , threading
balance = 0
lock = threading.Lock()
def change_it(n) :
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n) :
    for i in range(1000000) :
        lock.acquire() # 获取锁 ,保证改线程不被打断
        try :
            change_it(n)
        finally :
            lock.release() # 最后一定要释放锁

if __name__ == '__main__' :
    t1 = threading.Thread(target=run_thread,args=(5,))
    t2 = threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

