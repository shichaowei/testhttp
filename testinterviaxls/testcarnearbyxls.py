#coding:utf-8
'''
Created on 2015 12 28
@author: weishichao
'''

import json
from testbaseurl import *
import httplib, urllib
import time
import xlrd
import sys
import logging

xlsfile1 = r'F:/testexcel/testcarnearby.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

    
def testcarnearbyexcel(xlsfile=xlsfile1):
    
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
        priceRange= api_sheet.cell_value(i,3)
        brand= api_sheet.cell_value(i,4)
        models= api_sheet.cell_value(i,5)
        sorts= api_sheet.cell_value(i,6)
        secretkey = api_sheet.cell_value(i,7)
        
        ex_code = api_sheet.cell_value(i,8)
        #print ex_code
        ex_message=api_sheet.cell_value(i,9)
        #print ex_message
        
        datatemp={'latitude':latitude,'longitude':longitude,'offset':offset,\
                  'priceRange':priceRange,'brand':brand,'models':models,'sorts':sorts,'secretkey':secretkey}
        #print datatemp
        #print data1
        url='/car/nearby'

        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    testcarnearbyexcel(xlsfile1)
    