#coding:utf-8
'''
Created on 2015��12 27 
返回可开发票的订单列表(包含已开 和未开)。
@author: Administrator
'''

import json
import httplib, urllib
import time
import testbaseurl
import xlrd
import sys
from testbaseurl import *
#import WConio
import logging

xlsfile1 = r'F:/testexcel/testBillingCheck.xlsx'
reload(sys)
sys.setdefaultencoding('utf-8')



            
def testBillingCheck(xlsfile=xlsfile1):
    #logging.debug('\n')
    printtitle('START')
    #print "START USERGET"
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        uid = api_sheet.cell_value(i,0)   
        #print mobile
        token = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        
        orderIds = api_sheet.cell_value(i,3)
        
        orderIdstemp=str(orderIds)


        orderIds=orderIdstemp.split(',')
        print orderIds

        ex_code = api_sheet.cell_value(i,4)
        
        
        datatemp={'uid':uid,'token':token,'secretkey':secretkey,'orderIds':orderIds}
        print datatemp
        
        url='/invoice/billingcheck'
        testcodework(datatemp, url, ex_code)
        
        
                    
if __name__=="__main__":
    testBillingCheck(xlsfile1)
    
