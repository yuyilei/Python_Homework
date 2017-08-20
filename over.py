#!/usr/bin/env python
# encoding: utf-8
import threading , multiprocessing

def loop() :
    x = 0
    while True :
        x *= 1

for i in range(multiprocessing.cpu_count()) :
    t = threading.Thread(target=loop)
    t.start()

# 可以看到活动监视器上python的CPU占用率达到了99.8% 虽然是4核的CPU，但是CPU占用率最多也只能达到100%
# 这是因为解释器在执行python时。有一个GIL锁，Global Interpreter Lock ， python线程在执行前必须先获得GIL锁
# 每100字节的代码，解释器就自动释放GIL锁，GIL全局锁实际上把所有的线程的执行代码都上了锁，所有多线程的python只能交替执行
# 利用python执行多任务时，可以利用多进程来实现多核任务


