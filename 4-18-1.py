#尾递归，但是栈还是会溢出啊啊id
def fact(n) :
    return fact_iter(n,1)

def fact_iter(number,pro) :
    if number == 1 :
        return pro
    return fact_iter(number-1,pro*number)

if __name__ == '__main__' :
    print fact(100)
