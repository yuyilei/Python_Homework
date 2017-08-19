#!/usr/bin/env python
# encoding: utf-8
from multiprocessing import Pool
import os , time , random

def long_time_task(name) :
    print ('Run task %s (%s)'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() *3 )
    end = time.time()
    print ('Task %s runs %0.2f second.'%(name,(end-start)))

if __name__ == '__main__' :
    print('Parent process %s'% os.getpid())
    p = Pool(5) # 线程池 ，可以同时跑5个线程
    for i in range(5) :
        p.apply_async(long_time_task,args=(i,)) # 传输不定参数，非阻塞，支持结果返回后进行回调，在主进程循环中不等待apply_async的返回结果
    print ('Waiting for all subprocesses dose...')
    p.close() # 关闭pool，使其不再接受新的任务
    p.join() # 主进程阻塞等待子进程的退出，要在close或terminate之后使用
    print ('All subprocesses done.')
