
def add(former,later) :
    return former + later


def tell(number) :
    if 100>= number >= 90 :
        print 'A'
    elif 90 > number >= 80 :
        print 'B'
    elif 80 > number >= 70 :
        print 'C'
    elif 70 > number >= 60 :
        print 'D'
    elif 60 > number :
        print 'E'


def tellyear(year) :
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                print 'Yes'
            else :
                print 'No'
        else :
            print 'Yes'
    else  :
        print 'No'


def change(cent) :
    cent25  = cent % 25 
    cent25 = cent - 25 * cent25 
        cent10 = cent % 10 
        cent = cent - 10 * cent10
        cent5 = cent % 5 
        cent = cent - 5 * cent5
        cent1 = cent 
print 'cent25 cent10 cent5 cent1\n'

def count1(expression) :
    return eval(expression)

def count2(expression) :


def volume1(a,b ,c) :
    return a*b*c


import math 
def volume(r) :
    res = 4*r*r*r*math.pi/3
    return round(res,,4)

    return 4*

