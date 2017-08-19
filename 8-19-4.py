#!/usr/bin/env python
# encoding: utf-8

from multiprocessing import Process , Queue # multiprocessing 封装了fork函数，创建子进程
import os , time , random

def write(q) :
    print('Process to write : %s' %os.getpid() )
    for value in ['A','B','C'] :
        print ('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q) :
    print ('Process to read : %s' % os.getpid() )
    while True :
        value = q.get(True) # get的可选参数为block，默认参数为True，当队列为空，且block为True时，get()就调整线程暂停，直到有项目可用，如果为False则引发Empty异常
        print('Get %s from queue.'% value)

if __name__ == '__main__' :
    q = Queue()
    pw = Process(target=write,args=(q,)) # 调用对象为target
    pr = Process(target=read,args=(q,))
    pw.start() # 启动子进程，写入
    pr.start() # 启动子进程，读入
    pw.join() # 等待pw 结束
    pr.terminate() # pr进程进入死循环，无法结束，强制终止
