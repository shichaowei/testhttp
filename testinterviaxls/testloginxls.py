#coding:utf-8
'''
Created on 2015��11��10��

@author: Administrator
'''

import json
import httplib, urllib
import time
import sys
import xlrd
from testbaseurl import printtitle,printandlog,testcodework,urlpost
import logging


xlsfile1 = r'F:/testexcel/testlogin.xls'
reload(sys)
sys.setdefaultencoding('utf-8')



def testloginexcel(xlsfile=xlsfile1):
    
    printtitle('START testlogin')
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        mobile = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        password = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        ex_code = api_sheet.cell_value(i,3)
        #print ex_code
        ex_message=api_sheet.cell_value(i,4)
        #print ex_message
        
        datatemp = {'mobile':mobile,'passwd':password,'secretkey':secretkey}  #三个参数的值作为请求接口时要带上的数据
        url='/user/login'
        
        testcodework(datatemp, url, ex_code)
        
            
if __name__=="__main__":  
    testloginexcel(xlsfile1)
