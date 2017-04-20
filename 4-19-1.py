#coding: utf-8
#生成器，输出杨辉三角形
def triangle(n) :
    b = [1]
    t = 0
    while t < n  :
        b = [1] + [ b[i] + b[i+1] for i in range(len(b)-1)] + [1]
        t += 1
        yield(b)

n = input()
for t in triangle(n) :
    print t
