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

xlsfile1 = r'F:/testexcel/testwaldaybook.xls'
reload(sys)
sys.setdefaultencoding('utf-8')


            
            
def testwaldaybookexcel(xlsfile=xlsfile1):
    
    printtitle('START testwaldaybookexcel')
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    ncols=api_sheet.ncols
    print ncols
    
    for i in range(1,nrows):
        uid = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        token = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        offset=api_sheet.cell_value(i,3)
        ex_code = api_sheet.cell_value(i,4)
        ex_message=api_sheet.cell_value(i,5)
        #print ex_message
        
        datatemp={'uid':uid,'token':token,'secretkey':secretkey,'offset':offset}
        
        #print data1
        url='/wallet/daybook'
        testcodework(datatemp, url, ex_code)
        #api_sheet.put_cell(i,ncols,1,resultemp,0)
                            
if __name__=="__main__":
    testwaldaybookexcel(xlsfile1)
    