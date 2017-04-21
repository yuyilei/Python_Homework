#coding: utf-8
from  functools import reduce
# str -> int
def str2int(s) :
    def add (x,y) :
        return x*10 + y
    def char2int(s) :
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(add,map(char2int,s))

a = str2int('23834783')
print a , type(a)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def change2name(s) :
    def name(n) :
        return n.title()
    return map(name,s)

name = ['adam', 'LISA', 'barT']
print change2name(name)

#接受一个list，求乘积
def muti(s) :
    def x(a,b) :
        return a * b
    return reduce(x,s)

l = [2,43,32]
print muti(l)

# str -> float
def str2float(s) :
    def get(s) :
        d = s.find('.')
        res = s[:d] + s[d+1:]
        d = len(s) - d - 1
        return res , d
    def char2int(s) :
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def add(x,y) :
        return x*10+y
    return (float)(reduce(add,map(char2int,get(s)[0])))/(10**get(s)[1])

print str2float('123.1234')
