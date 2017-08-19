#!/usr/bin/env python
# encoding: utf-8
import os
print ('Process (%s) start...'% os.getpid())
pid = os.fork()
if pid == 0 :
    print ('child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else :
    print ('parent process (%s) just created a child process (%s) '% (os.getpid(),pid))

