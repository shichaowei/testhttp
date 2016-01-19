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
from testbaseurl import printtitle,printandlog,testcodework
import logging

xlsfile1 = r'F:/testexcel/testchangepwd.xls'
reload(sys)
sys.setdefaultencoding('utf-8')



def testchangepwdexcel(xlsfile=xlsfile1):
    printtitle('START CHANGPWD')
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        uid = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        token = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        oldpwd=api_sheet.cell_value(i,3)
        newpwd=api_sheet.cell_value(i,4)
        ex_code = api_sheet.cell_value(i,5)
        #print ex_code
        ex_message=api_sheet.cell_value(i,6)
        #print ex_message
        #print newpwd
        
        datatemp={'uid':uid,'oldpwd':oldpwd,'newpwd':newpwd,\
               'token':token,'secretkey':secretkey}
        #print data1
        url='/user/changepwd'
        testcodework(datatemp, url, ex_code)
      
if __name__=="__main__":
    testchangepwdexcel(xlsfile1)
    