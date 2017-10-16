#coding: utf-8 
""" 

    Python的在3.4中引入了协程的概念，这个还是以生成器对象为基础，3.5则确定了协程的语法。 
    event_loop 事件循环：程序开启一个无限的循环，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    coroutine协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
    task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态，用于获取未来协程的结果。
    future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别,相当于一个占位符，其值会在将来被计算出来。
    async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
    当遇到阻塞调用的函数的时候，使用await方法将协程的控制权让出，以便loop调用其他协程。

    并发和并行，举个例子，并发是一个妈妈用一个勺子同时给哥哥和弟弟喂饭，哥哥喂一口。弟弟喂一口，并行是妈妈用两个勺子给同时个哥哥和弟弟喂饭，
    哥哥和弟弟同时吃饭。 
    asyncio实现并发，需要多个协程来完成任务，每当有任务阻塞就await，然后其他协程继续工作。创建多个协程的列表，将这些协程注册到事件循环中。 

"""

import asyncio 
import functools

def done_callback(loop,futu) :
    print('End at {}'.format(loop.time()))
    loop.stop()

  #  run_forever 永远执行，用stop停止它，用close关闭它
  #  不要在一个协程里面停止loop，因为别的协程可能还没停止，所以用gather把多个协程合并成一个future，添加会调，在回调函数停止loop 


async def do_somework(loop,x) : 
    print('Waiting {}'.format(x)) 
    await asyncio.sleep(x)
    print('Done {} at {}'.format(x,loop.time()))

loop = asyncio.get_event_loop()
print('Start at {}'.format(loop.time()))
coroutines = [ 
     do_somework(loop,1) , 
     do_somework(loop,2) , 
     do_somework(loop,3) 
]

tasks = [ asyncio.ensure_future(coroutine) for coroutine in coroutines ]
futus = asyncio.gather(task for task in tasks) 
#futus = asyncio.gather(do_somework(loop,1),do_somework(loop,2),do_somework(loop,3))
futus.add_done_callback(functools.partial(done_callback,loop))
loop.run_forever()