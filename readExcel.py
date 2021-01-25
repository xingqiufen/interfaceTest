# -*- coding: utf-8 -*-
"""
@Auth ： xingqiufen
"""

import xlrd,os
from commonMethod.baseInfo import rootDir
from commonMethod import commonWays
from xlutils.copy import copy
import json

excelDir=r'testData\testExcel.xls'
excelPath=rootDir+excelDir


def readExcel(excelPath):
    if os.path.exists(excelPath):# 判断路径是否存在
        workBook=xlrd.open_workbook(excelPath,formatting_info=True)
        # 获取所有的sheets
        workSheets=workBook.sheets()
        # 获取测试用例所在的sheet
        workSheet=workBook.sheet_by_name('Sheet1')
        # 取参数传递数据值
        cellData=workSheet.cell(1,6)
        # print(cellData)
        # return cellData
        # body=cellData['tel']=f'158{random.randint(11111111,99999999)}'
        response=commonWays.findTel2(str(cellData))
        # print(response)
        # print(type(json.dumps(str(response))),response)
        # print(r'response'+"['catName']:",response['catName'])
        # return response
        if '中国移动' in response:
            info='通过'
        else:
            info='失败'
        #拷贝excel对象
        newworkBook = copy(workBook)
        newSheet=newworkBook.get_sheet(0)
        print(newSheet)
        newSheet.write(1,8,response)
        newSheet.write(1,9,info)
        newworkBook.save(rootDir+r'testData\testExcel111.xls')
    else:
        return "测试用例文件不存在！"

if __name__ == '__main__':
    readExcel(excelPath)
    # print(readExcel(excelPath))















