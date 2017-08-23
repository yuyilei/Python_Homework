#!/usr/bin/env python
# encoding: utf-8

import os
class Expression(object) :
    def __init__(self,express) :
        self.express = express
        self.postfix = []

    def get_postfix(self) :
        ex = self.express
        stack = []
        numbers = "0123456789"
        sign = "()+-*/"
        tmp = ""
        after = []
        for item in ex :
            if item in numbers :
                if len(tmp) == 0 :
                    tmp = item
                    continue
                tmp += item
            elif item in sign :
                after.append(tmp)
                tmp = ""
                after.append(item)
        if tmp != "" :
            after.append(tmp)

        for item in after :
            if item not in sign :
                self.postfix.append(float(item))
            elif item != '' :
                if len(stack) == 0 :
                    stack.append(item)
                    continue
                top = stack[-1]
                if item == ')':
                    while True :
                        top = stack.pop()
                        if top == '(' :
                            break
                        self.postfix.append(top)
                elif top in "*/" and  item in "+-" :
                    while len(stack) != 0 :
                        self.postfix.append(stack.pop())
                    stack.append(item)
                else :
                    stack.append(item)
        while len(stack) != 0 :
            self.postfix.append(stack.pop())

    def get_res(self) :
        stack = []
        sign = '+-*/'
        postfix  = self.postfix
        for item in postfix :
            if isinstance(item,float) :
                stack.append(item)
            else :
                latter = stack.pop()
                former = stack.pop()
                if item == '+' :
                    res = former+latter
                elif item == '-' :
                    res = former-latter
                elif item == '*' :
                    res = former*latter
                elif item == '/' :
                    if latter == 0 :
                        print('Error!')
                        os._exit()
                    res = former/latter
                stack.append(res)
        res = self.express + ' ==> '+str( [str(res),int(res)][int(res)==res])
        print (res)

if __name__ == '__main__' :
    express = Expression(raw_input("输入一个表达式\n"))
    express.get_postfix()
    express.get_res()



