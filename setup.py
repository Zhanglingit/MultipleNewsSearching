#! /usr/bin/env python
#coding=utf8


from distutils.core import setup
import py2exe,sys


sys.path.append(r'D:\Documents\pythonworkplace\py2exe_lee')

setup(
options = {'py2exe':{
                    'compressed':1,
                    'optimize':2,
                    'bundle_files':1,}},
#zipfile = Yes,
console=["jfLibGoogle.py"]
)

