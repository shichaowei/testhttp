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

xlsfile1 = r'F:/testexcel/testpaypre.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

    
def testpaypreexcel(xlsfile=xlsfile1):
    
    title='START TESTstationnearby'
    printtitle(title)
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        orderId = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        amount = api_sheet.cell_value(i,1)
        #print password
        payType = api_sheet.cell_value(i,2)
        bsType= api_sheet.cell_value(i,3)
        uid= api_sheet.cell_value(i,4)
        token= api_sheet.cell_value(i,5)
        secretkey= api_sheet.cell_value(i,6)
        
        ex_code = api_sheet.cell_value(i,7)
        #print ex_code
        ex_message=api_sheet.cell_value(i,8)
        #print ex_message
        
        datatemp={"orderId":orderId,'amount':amount,'payType':payType,\
               "bsType":bsType,\
              "uid":uid,"token":token,"secretkey":secretkey}
   
        #print data1
        url='/pay/prepay'

        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    testpaypreexcel(xlsfile1)
    