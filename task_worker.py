#!/usr/bin/env python
# encoding: utf-8

import time , sys , queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager) :
        pass

if __name__ == '__main__' :
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    server_addr = input('input the IPAddress\n')
    print ('Connect to server %s...'% server_addr)
    # 连接到服务器
    m = QueueManager(address=(server_addr,5000),authkey=b'abc')
    # 从网络连接
    m.connect()
    # 获取Queue对象
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 执行任务
    for i in range(10) :
        try :
            n = task.get(timeout=1)
            print('run task %d * %d ' % (n,n))
            r = '%d * %d = %d' % ( n , n , (n *n ))
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')
    print ('worker exit.')

