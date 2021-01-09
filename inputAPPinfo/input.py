# coding=utf-8

import xml.dom.minidom
import re
import os

# 打开xml文档
dom = xml.dom.minidom.parse('input/input.xml')

# 得到文档元素对象
root = dom.documentElement

item = root.getElementsByTagName("item")

for item in item:
    compoent = item.getAttribute("component")
    strlist = re.split('[/{}]',compoent)
    rewrite = strlist[1].replace(".", "_")
    drawable =rewrite.lower()
    filename = 'output/' + rewrite + '.xml'
    iteminfo = '<item component="' + compoent + '" drawable="' + drawable + '" />\n'
    with open(filename, 'a') as file_object:
        file_object.write(iteminfo)
    print ("Add Icon Success")

print("Finish!")
