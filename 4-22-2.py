#coding: utf-8
#利用filter输出回文数
def is_palindrome(n) :
    n = str(n)
    return n == n[::-1]

output = filter(is_palindrome,range(0,1000))
for i in list(output) :
    print(i)

