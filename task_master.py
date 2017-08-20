#!/usr/bin/env python
# encoding: utf-8

import random , time , queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()  # 发送任务的队列
result_queue = queue.Queue()

class QueueManager(BaseManager) :
    pass

if __name__ == '__main__' :
    # 将2个Queue注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=lambda:task_queue)
    QueueManager.register('get_result_queue',callable=lambda:result_queue)
    # 绑定5000 端口 ,设置验证吗
    manager = QueueManager(address=('',5000),authkey=b'abc')
    #启动
    manager.start()
    #  通过网络访问Queue对象
    # 疑问？为什么在本机要通过网络访问Queue 对象？？ 难道他们不在一个进程内？？
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10) :
        n = random.randint(0,10000)
        print('Put task %d...'% n)
        task.put(n)

    #读取
    print ('Try get results...')
    for i in range(10) :
        r = result.get(timeout=100)
        print('Result: %s'%r)
    # 关闭
    manager.shutdown()
    print('master exit.')


