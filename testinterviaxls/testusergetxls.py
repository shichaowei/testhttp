#coding:utf-8
'''
Created on 2015��12 21 

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

xlsfile1 = r'F:/testexcel/testuserget.xls'
reload(sys)
sys.setdefaultencoding('utf-8')



            
def testusergetexcel(xlsfile=xlsfile1):
    #logging.debug('\n')
    printtitle('START userget')
    #print "START USERGET"
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
        ex_message=api_sheet.cell_value(i,4)
        
        datatemp={'uid':uid,'token':token,'secretkey':secretkey}
        
        url='/user/get'
        testcodework(datatemp, url, ex_code)


                        
if __name__=="__main__":
    testusergetexcel(xlsfile1)
    
