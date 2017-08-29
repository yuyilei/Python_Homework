#!/usr/bin/env python
# encoding: utf-8

import requests
source = str(input("input the ways"))
r = requests.post("https://cuntuku.com/api/1/upload/?key=584bf3b4398f4e01f695cc0c50253110&source=file://" + source + "&format=json")
print (r.text)

