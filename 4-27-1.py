#coding: utf-8
#迭代器生成斐波那契数列
class Fib :
    def __init__(self) :
        self.prev = 0
        self.curr = 1
    def __iter__(self) :
        return self
    def __next__(self) :
        temp = self.curr
        self.curr += self.prev
        self.prev = temp
        return temp

f = Fib()
from itertools import islice
l = list(islice(f,0,10))
for i in l :
    print(i)

