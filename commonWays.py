# -*- coding: utf-8 -*-
"""
@Auth ： xingqiufen
"""

import requests
import json

def findTel2(body):
  url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=15850781443"
  payload =body #body.json()#json.loads(body)
  headers = {'key': '03ffe3fd839110a87b4d884497c46c73'}
  response = requests.get(url=url,json=payload,headers=headers)
  # print(response.text)
  return response.text.split('=')[1]#['catName']
    #json.dumps(response.text)
    # response.text
  #json.dumps(response.text)
    #type(response.text)


body={'tel': '15811345218'}
print(findTel2(body))