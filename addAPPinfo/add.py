# -*- coding: utf-8 -*-

import os

file_dir = './input'

for root, dirs, files in os.walk(file_dir):
    for item in files:
        packname = item[:-4]
        rewrite = packname.replace('.','_')
        drawable = rewrite.lower()
        drawable_name = drawable + '.png'
        print (drawable)
        print (drawable_name)
        resources_name = 'resources/'+ drawable + '.xml'
        print (resources_name)
        if (os.path.exists(resources_name)):
            print('Find resources successfully')
            print('Begin write')
            resources_file = open(resources_name, 'r')
            print('Open file Success')
            output_appfilter = open('output/appfilter.xml', 'a')
            output_appfilter.write(resources_file.read())
            print('Add appfilter success')
            old_drawable_path = 'input/' + item
            old_drawable_path_name = 'output/drawable/' + drawable_name
            drawable_name_output = os.rename(old_drawable_path,old_drawable_path_name)
            print('Rename drawable name success')
            print('Move drawable success')
            output_drawable = open('output/drawable.xml', 'a')
            iteminfo = '<item drawable="' +  drawable + '" name="' + packname + '" />\n'
            output_drawable.write(iteminfo)
            print('Write Drawable successfully')


        else:
            print('Have no resources')


input()
