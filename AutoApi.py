#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import re

class Api() :
    def __init__(self,root,api) :
        self.root = root
        self.api = api

    def static_content(self,fapi) :
        OutputList = \
            ['from flask import jsonify , g , request , current_app \n',
            'from .. import                \n',
            'from .. import db             \n']
        fapi.writelines(OutputList)

    def get_blueprint(self) :
        root  = self.root
        api = self.api
        for  each in root :
            os.chdir(root)
            init = open("__init__.py","r")
            lines = init.readlines()
            for index , line in enumerate(lines) :
                if "Blueprint" in line :
                    temp  = lines[index+1]
                    blue = ''
                    flag = 0
                    for j , i in enumerate(temp) :
                        if temp[j] == '\'' and flag != 0 :
                            break
                        if flag == 1  :
                            blue += i
                        if i == '\'' :
                            flag += 1
                    self.blue = blue

    def generate_api(self) :
        root = self.root
        api = self.api
        print root
        for each in root :
            os.chdir(root)
            for item in api :
                fapi = open(item+".py","w+")
                self.static_content(fapi)
                fapi.close()

def find_init() :
    API = []
    for root , dirs , files in os.walk(".") :
        for each in files :
            if each == '__init__.py' :
                init = open(root+"/"+each,'r')
                lines = init.readlines()
                for index , line in enumerate(lines) :
                    if "from" in line and "." in line and "import" in line :
                        if '\\' in line :
                            flag = 1
                        _api = re.split(",",line)
                        first = _api[0].split()[-1]
                        api_ = _api[1:]
                        api_ = api_[:-1]
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
                        api = list(set(api))
                        path = os.getcwd() + root[1:]
                        item = Api(path,api)
                        API.append(item)
                init.close()
    if len(API) == 0 :
        print "Can not find __int__.py"
        sys.exit(0)
    return API


if  __name__ == '__main__' :
    api  = find_init()
    for each in api :
        each.generate_api()
        each.get_blueprint()


