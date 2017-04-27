#coding: utf-8
#生成器，斐波那契数列
def fib() :
    prev , curr = 0 , 1
    while True :
        prev , curr = curr , curr + prev
        yield prev

f = fib()
from itertools import islice
l = list(islice(f,0,10))
print(l)
