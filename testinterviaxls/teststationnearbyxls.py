#coding:utf-8
'''
Created on 2015 11 17
test 获取离当前位置最近网点信息（列表）接口
@author: weishichao
'''

import json
from testbaseurl import *
import httplib, urllib
import time
import xlrd
import sys
import logging

xlsfile1 = r'F:/testexcel/teststationnearby.xls'
reload(sys)
sys.setdefaultencoding('utf-8')
#false='false' #此处是因为false和true和null，eval不转换，需要加上此语句才可以

    
def teststationnearbyexcel(xlsfile=xlsfile1):
    
    title='START TESTstationnearby'
    printtitle(title)
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        latitude = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        longitude = api_sheet.cell_value(i,1)
        #print password
        offset = api_sheet.cell_value(i,2)
        secretkey = api_sheet.cell_value(i,3)
        
        ex_code = api_sheet.cell_value(i,4)
        #print ex_code
        ex_message=api_sheet.cell_value(i,5)
        #print ex_message
        
        datatemp={'latitude':latitude,'longitude':longitude,'offset':offset,'secretkey':secretkey}
        #print datatemp
        #print data1
        url='/station/nearby'

        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    teststationnearbyexcel(xlsfile1)
    