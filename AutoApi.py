#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import re

class Models() :
    def __init__(self,path,models) :
        self.path = path
        self.models = models

    def get_models(self) :

class Api() :
    def __init__(self,root,api) :
        self.root = root
        self.api = api

    def static_content(self,fapi,api) :
        api = api+'.py'
        OutputList = \
            ['#coding:utf-8\n\n\n',
            ' \'\'\' ' ,
            ' ********************************** \n\n ' ,
            '           ' ,
            api ,
            '\n\n',
            ' **********************************  ' ,
            '\'\'\' ' ,
            '\n\n\n' ,
            'from flask import jsonify , g , request , current_app \n',
            'from flask_login import current_user\n' ,
            'from ..models import db \n' ,
            'import json\n' ,
            'import request\n'
             ]
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

    def import_models(self,models,fapi) :
        model = (' , ').join(models.models)
        Output =  ["from ..models  import " + model+"\n" ]
        fapi.writelines(Output)

    def import_blueprint(self,fapi) :
        Output = ["from . import " + self.blue +"\n\n\n\n\n\n"]
        fapi.writelines(Output)

    def to_get(self,fapi) :
        Output = ['@'+self.blue+'.route(\' \', methods=[\'GET\'])       \n' ,
                  'def                                      \n ' ,
                  '   \'\'\'\n    description of function\n    \'\'\'\n ' ,
                  '\n\n' ,
                  '    return jsonify ({ \n\n              }) '  ,
                  ',    \n\n\n\n' ,
                  ]
        fapi.writelines(Output)

    def to_post(self,fapi) :
        Output = ['@'+self.blue+'.route(\' \', methods=[\'POST\'])       \n' ,
                  'def                                      \n ' ,
                  '   \'\'\'\n    description of function\n    \'\'\'\n ' ,
                  '\n\n' ,
                  '    db.session.add() \n' ,
                  '    db.session.commit() \n',
                  '    return jsonify ({ \n\n              }) '  ,
                  ',    \n\n\n\n' ,
                  ]
        fapi.writelines(Output)

    def to_put(self,fapi) :
        Output = ['@'+self.blue+'.route(\' \', methods=[\'PUT\'])       \n' ,
                  'def                                      \n ' ,
                  '   \'\'\'\n    description of function\n    \'\'\'\n ' ,
                  '\n\n' ,
                  '    db.session.add() \n' ,
                  '    db.session.commit() \n',
                  '    return jsonify ({ \n\n              }) '  ,
                  ',    \n\n\n\n' ,
                  ]
        fapi.writelines(Output)


    def to_delete(self,fapi) :
        Output = ['@'+self.blue+'.route(\' \', methods=[\'DELETE\'])       \n' ,
                  'def                                      \n ' ,
                  '   \'\'\'\n    description of function\n    \'\'\'\n ' ,
                  '\n\n' ,
                  '    db.session.delete() \n' ,
                  '    db.session.commit() \n',
                  '    return jsonify ({ \n\n              }) '  ,
                  ',    \n\n\n\n' ,
                  ]
        fapi.writelines(Output)



    def generate_api(self,models) :
        root = self.root
        api = self.api
        print root
        for each in root :
            os.chdir(root)
            for item in api :
                if not os.path.isfile(item+".py") :
                    fapi = open(item+".py","w+")
                    self.static_content(fapi,item)
                    self.import_models(models,fapi)
                    self.import_blueprint(fapi)
                    self.to_get(fapi)
                    self.to_get(fapi)
                    self.to_post(fapi)
                    self.to_post(fapi)
                    self.to_put(fapi)
                    self.to_delete(fapi)
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

def find_models() :
    models = []
    path = '1'
    for root , dirs , files in os.walk(".") :
        for each in files :
            if each == 'models.py' :
                path = root
                init = open(root+"/"+each,'r')
                lines = init.readlines()
                for line in lines :
                    if line[:5] == 'class' :
                        item = ''
                        for i in line[6:] :
                            flag = 0
                            if i != ' ' :
                                flag = 1
                            if i == "(" or i == ':' :
                                break
                            if flag == 1:
                                item += i
                        models.append(item)
    Model = Models(path,models)
    return Model

if  __name__ == '__main__' :
    api  = find_init()
    model = find_models()
    model.get_models()
    for each in api :
        each.get_blueprint()
        each.generate_api(model)


