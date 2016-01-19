#coding:utf-8
'''
Created on 2015��12 21 

@author: Administrator
'''

import json
import httplib, urllib
import time
import xlrd
import sys
from testbaseurl import *
import logging

xlsfile1 = r'F:/testexcel/testusergetauth.xls'
reload(sys)
sys.setdefaultencoding('utf-8')



            
def testusergetauthexcel(xlsfile=xlsfile1):
    
    printtitle('START TESTusergetauth')
    
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
        
        url='/user/getauth'

        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    testusergetauthexcel(xlsfile1)
    
