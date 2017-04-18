def my_abs(n) :
    if not isinstance(n,(int,float)) :
        raise TypeError("tppeerror!!")
    if n > 0 :
        return n
    else :
        return -n

import math
def quadratic(a,b,c) :
    if not isinstance(a,(int,float)) :
        raise TypeError("Error A!")
    if not isinstance(b,(int,float)) :
        raise TypeError("Error B!")
    if not isinstance(c,(int,float)) :
        raise TypeError("Error C!")
    s  = b*b - 4*a*c
    if s < 0 :
        return None
    x1 = (-b+math.sqrt(s))/(2*a)
    x2 = (-b-math.sqrt(s))/(2*a)
    return x1 , x2
def func(num=1) :
    pass # 默认参数必须是不可变的，不能是列表！！！
def func1(*num) :
    pass  #可变参数！！！！接受一个元组
def func2(num) :
    pass # 可传入元组和列表23333
def func3(one,two,**kw) :
    pass #kw是关键词参数，可变的2333，自动生成一个字典
def func4(one,two,*,other,anothr) :
    pass # * 规定了关键词参数只能是*后面的other和another ,关键词参数必须传入参数名
if __name__ == '__main__' :
    n = input("input a number")
    print((my_abs(int(n))))
    print(quadratic(1,2,1))
    print(quadratic(1,3,1))
    print(quadratic(1,'a',1))
    print(quadratic('a',2,1))
    print(quadratic(1,2,-1))
    print(quadratic(1,2,'c'))

