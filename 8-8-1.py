#!/usr/bin/env python
# encoding: utf-8

class read(object) :
    def __init__(self,num) :
        self.num = num
        self.sumup = 0

    def sum_up(self) :
        number = self.num
        while ( number != 0 ) :
            self.sumup += number % 10
            number /= 10
        print self.num,"的各位数总和是",self.sumup

    def print_out(self) :
        num_list = [ 'yi','er','san','si','wu','liu','qi','ba','jiu']
        sumup = self.sumup
        res = []
        while sumup != 0 :
            index = (sumup % 10) - 1
            res.append(num_list[index])
            sumup /= 10
        res.reverse()
        out = ' '.join(res)
        print self.sumup ,"的拼音是",out

    def change(self) :
        tmp = self.sumup % 3 + self.sumup % 5 + 2
        res = []
        sumup = self.sumup
        while sumup != 0 :
            res.append(str(sumup % tmp))
            sumup /= tmp
        res.reverse()
        out = ''.join(res)
        print self.sumup ,"转化为",tmp,"进制是",out

if __name__ == '__main__' :
    number = read(input("输入一个尽可能长的数字\n"))
    number.sum_up()
    number.print_out()
    number.change()


