#coding:utf-8
'''
Created on 2015 11 17
test 获取用户基本信息接口
@author: weishichao
'''

import json
import httplib, urllib
import time
from testbaseurl import *
import time
import xlrd
import sys
import logging

xlsfile1 = r'F:/testexcel/teststationdetail.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

 
def teststationdetexcel(xlsfile=xlsfile1):
    printtitle('START testchangepwdexcel')
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        testid = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        secretkey = api_sheet.cell_value(i,1)
        ex_code = api_sheet.cell_value(i,2)
        #print ex_code
        ex_message=api_sheet.cell_value(i,3)
        #print ex_message
        
        datatemp={'id':testid,'secretkey':secretkey}
        
        #print data1
        url='/station/detail'
        testcodework(datatemp, url, ex_code)
                                    
if __name__=="__main__":
    teststationdetexcel(xlsfile1)  
    
    