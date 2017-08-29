#!/usr/bin/env python
# encoding: utf-8

class read(object) :
    def __init__(self,num) :
        self.num = int(num)
        self.sumup = 0

    def sum_up(self) :
        number = self.num
        while int(number)  :
            self.sumup += number % 10
            number //=  10
        print ("%d的各位数总和是%d" % (self.num,self.sumup) )

    def print_out(self) :
        num_list = [ 'yi','er','san','si','wu','liu','qi','ba','jiu']
        sumup = int(self.sumup)
        res = []
        while int(sumup)   :
            index = int((sumup % 10) - 1)
            res.append(num_list[index])
            sumup //= 10
        res.reverse()
        out = ' '.join(res)
        print ("%d的拼音是%s" % ( self.sumup,out))

    def change(self) :
        tmp = 7
        res = []
        sumup = self.sumup
        while int(sumup)  :
            res.append(str(int(sumup) % tmp))
            sumup //= tmp
        res.reverse()
        out = ''.join(res)
        print ("%d转化为7进制是%s" % (self.sumup, out))

if __name__ == '__main__' :
    number = read(input("输入一个尽可能长的数字\n"))
    number.sum_up()
    number.print_out()
    number.change()


