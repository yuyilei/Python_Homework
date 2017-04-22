#coding: utf-8
#利用filter筛选得到1000以内的素数,要用python3
def _odd_iter(m):
    n = 1
    while n < m :
        n = n + 2
        yield n
def _not_divisible(n):
     return lambda x: x % n > 0
def primes(m):
    yield 2
    it = _odd_iter(m) # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), list(it))# 构造新序列)))))
m = int(input())
for n in primes(m):
    if n < 1000:
        print(n)
    else:
        break
