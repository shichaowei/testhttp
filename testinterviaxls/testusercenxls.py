#coding:utf-8
'''
Created on 2015��11��10��

@author: Administrator
'''

import json
import httplib, urllib
import time
import xlrd
import sys
import logging
from testbaseurl import urlpost,printtitle,printandlog,testcodework
import logging

xlsfile1 = r'F:/testexcel/testusercenter.xls'
reload(sys)
sys.setdefaultencoding('utf-8')


            
            
def testusercenexcel(xlsfile=xlsfile1):
    
    printtitle('START testusercenexcel')
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        uid = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        token = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        ex_code = api_sheet.cell_value(i,3)
        #print ex_code
        ex_message=api_sheet.cell_value(i,4)
        #print ex_message
        
        datatemp={'uid':uid,'token':token,'secretkey':secretkey}
        
        #print data1
        url='/user/center'
        testcodework(datatemp, url, ex_code)
                            
if __name__=="__main__":
    testusercenexcel(xlsfile1)
    