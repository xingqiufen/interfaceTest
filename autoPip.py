# -*- coding: utf-8 -*-
"""
@Auth ： xingqiufen
"""

'''
1. 读取配置文件
2. 执行安装哭的指令
3. 验证是否安装成功
4. 打印日志

'''

import os
import logging
log_format='%(asctime)s-%(levelname)s-%(message)s'
date_format='%Y-%m-%d %H:%M:%S'
# print("../testLog/testLog.log'",os.path.exists('../testLog/testLog.log'))
logDir='../testLog/testLog.log'
logging.basicConfig(filename=logDir,level=logging.DEBUG,format=log_format,datefmt=date_format)
# 打开配置文件
file=open('../testConfig/baseConfig.ini')
# 通过file.read.splitlines()方法得到配置文件所有数据的列表
listInfo=file.read().splitlines()

#查看已安装的库
installedKu=os.popen('pip list')
installedList=installedKu.read()
# print(installedList)

for info in listInfo:
    if info in installedList:
        logging.warning(info+"已经安装")
        #print(info+"已安装！")
    else:
        pipObject=os.popen(r'pip install ' + info)
        pipInfo=pipObject.read()
        if 'successfully' in pipInfo:
            logging.info('---'+info+"--安装成功！--")
            # print('---'+info+"--安装成功！--")
        else:
            logging.error('---' + info + "--安装失败！--")
            #print(info+'--安装失败！--')