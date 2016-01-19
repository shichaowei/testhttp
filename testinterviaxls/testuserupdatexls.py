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

xlsfile1 = r'F:/testexcel/testupdate.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

            
def testupdateexcel(xlsfile=xlsfile1):
    
    printtitle('START TESTupdate')

    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        uid = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        token = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        upic = api_sheet.cell_value(i,3)
        
        ex_code = api_sheet.cell_value(i,4)
        #print ex_code
        ex_message=api_sheet.cell_value(i,5)
        #print ex_message
        
        datatemp={"uid":uid,"token":token,'upic':upic,\
               "secretkey":secretkey}
        
        #print data1
        url='/user/update'
        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    testupdateexcel(xlsfile1)
    