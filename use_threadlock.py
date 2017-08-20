#!/usr/bin/env python
# encoding: utf-8
import threading # threading.local() 解决了同一个线程中各个函数之间传递参数的问题
local_school = threading.local() # 每个线程对local_school都可以读写student属性，但是不会影响
def process_student() :
    std = local_school.student # 获取当前线程相关联的student
    print ('Hello , %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name) :
    local_school.student = name # 绑定ThreadLocal的student
    process_student()

if __name__ == '__main__' :
    t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
    t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


