#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import re

def static_content() :
    OutputList = \
        ['from flask import jsonify , g , request\n',
         'from .. import                \n',
         'from .. import db             \n']
    fapi.writelines(OutputList)

def find_init() :
    roots = []
    apis = []
    for root , dirs , files in os.walk(".") :
        for each in files :
            if each == '__init__.py' :
                init = open(each,'r')
                lines = init.readlines()
                for index , line in enumerate(lines) :
                    if "from" in line and "." in line and "import" in line :
                        if '\\' in line :
                            flag = 1
                        _api = re.split(",",line)
                        first = _api[0].split()[-1]
                        api_ = _api[1:]
                        api_ = api_[:-2]
                        api_.append(first)
                        if  flag == 1 :
                            next_ = lines[index+1][:-1]
                            more = re.split(",",next_)
                            api_.extend(more)
                            flag = 0
                        api = []
                        for a in api_ :
                            a =  a.replace(' ','')
                            api.append(a)
                        roots.append(root)
                        apis.append(api)
    if len(roots) == 0 :
        print "Can not find __int__.py"
        sys.exit(0)
    return roots , apis


if  __name__ == '__main__' :
    roots , apis  = find_init()
    print roots
    print apis
    # with open("api/share.py","w+") as fapi :
    #    static_content()


