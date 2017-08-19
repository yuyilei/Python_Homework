#!/usr/bin/env python
# encoding: utf-8

import subprocess
print ('$$ nslookup www.python.org')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE) # 启动子进程
output , err = p.communicate(b'set q=mx\npython.org\nexit\n') # 相当于在子进程中输入
print (output.decode('utf-8'))
print ('Exit code :', p.returncode)
