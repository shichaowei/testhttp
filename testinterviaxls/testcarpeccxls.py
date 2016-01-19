#coding:utf-8
'''
Created on 2015��11��10��

@author: Administrator
'''

import json
from testbaseurl import *
import httplib, urllib
import time
import xlrd
import sys
import logging

xlsfile1 = r'F:/testexcel/testcarpeccancylist.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

            
def testpeccancylistexcel(xlsfile=xlsfile1):
    
    printtitle('START testpeccancylist')

    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        orderId = api_sheet.cell_value(i,0)
        status=api_sheet.cell_value(i,1)
        uid = api_sheet.cell_value(i,2)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        token = api_sheet.cell_value(i,3)
        #print password
        secretkey = api_sheet.cell_value(i,4)
        ex_code = api_sheet.cell_value(i,5)
        #print ex_code
        ex_message=api_sheet.cell_value(i,6)
        #print ex_message
        
        datatemp={'orderId':orderId,'status':status,"uid":uid,"token":token,\
               "secretkey":secretkey}
        
        #print data1
        url='/car/peccancylist'
        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    testpeccancylistexcel(xlsfile1)
    