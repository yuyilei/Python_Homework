#!/usr/bin/env python
# encoding: utf-8

from collections import namedtuple , deque , defaultdict , OrderedDict , Counter
Ponit = namedtuple('Point',['x','y'])
p = Ponit(1,2)
print (p.x)
print (p.y)
# 索引是自定义的x,y
q = deque(['x','y','z'])
q.append('a')
q.appendleft('b')
print (q)
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print (dd['key'] )
print (dd['key1'])
# 按照插入的顺序排列
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print (list(od.keys()))
# 计数器，计算各个字符出现的次数
c = Counter()
for ch in 'programing' :
    c[ch] += 1
print (c)
