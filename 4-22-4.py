def count () :
    def f(j) :
        def g() :
            return j*j
        return g
    fs  = []
    for i in range(1,4) :
        fs.append(f(i)) # 先把 i 存进去
    return fs

f1 , f2 , f3  = count()
print(f1(),f2(),f3()) # 调用函数的时候才是计算的时候

def count2() :
    def g(j) :
        return j*j
    fs = []
    for i in range(1,4) :
        fs.append(g(i))
    return fs

g1 , g2 , g3 = count2() #这样数不行的，因为返回的不是函数
print (g1(),g2(),g3())
