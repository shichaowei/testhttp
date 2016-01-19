#coding:utf-8
'''
Created on 2015 12 21

@author: Administrator
'''

import json
import httplib, urllib
import time
import xlrd
import sys
from testbaseurl import urlpost
from testbaseurl import printtitle,printandlog
from testbaseurl import *
import logging

xlsfile1 = r'F:/testexcel/testnearbydistance.xls'
reload(sys)
sys.setdefaultencoding('utf-8')



def testchangepwdexcel(xlsfile=xlsfile1):
    printtitle('START CHANGPWD')
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        latitude = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        longitude = api_sheet.cell_value(i,1)
        #print password
        distance = api_sheet.cell_value(i,2)
        secretkey=api_sheet.cell_value(i,3)
        ex_code = api_sheet.cell_value(i,4)
        #print ex_code
        ex_message=api_sheet.cell_value(i,5)
        #print ex_message
        #print newpwd
        
        datatemp={'latitude':latitude,'longitude':longitude,'distance':distance,\
                  'secretkey':secretkey}
        #print data1
        url='/station/nearbydistance'
        testcodework(datatemp, url, ex_code)
        
                        
if __name__=="__main__":
    testchangepwdexcel(xlsfile1)
    