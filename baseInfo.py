# -*- coding: utf-8 -*-
"""
@Auth ： xingqiufen
"""
import os
projectName='interfaceTest'
currentDir=os.getcwd()
rootDir=currentDir[:(currentDir.find(projectName)+len(projectName)+1)]
print(rootDir)
