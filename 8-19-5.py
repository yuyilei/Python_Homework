#!/usr/bin/env python
# encoding: utf-8
import  time , threading
#
def loop() :
    print ('thread %s is running...'% threading.current_thread().name) # current_thread返回当点线程的实例
    for n in range(5) :
        print ('thread %s >>> %s' % (threading.current_thread().name,str(n+1)))
    print ('thread %s end.' %  threading.current_thread().name)

if __name__ == '__main__' :
    print ('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop,name='LoopThread') # 启动一个线程，把一个函数传入并创建Thread实例，调用start开始
    t.start()
    t.join()
    print ('thread %s end.'%threading.current_thread().name)

# 多进程可以理解为不断创造实例来执行程序
# 多线程是不断向实例里添加函数来执行程序
