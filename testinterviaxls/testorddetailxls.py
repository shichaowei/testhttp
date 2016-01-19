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

xlsfile1 = r'F:/testexcel/testorddetail.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

 
def testorddetailexcel(xlsfile=xlsfile1):
    printtitle('START testorddetailexcel')
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        
        uid = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        token = api_sheet.cell_value(i,1)
        secretkey = api_sheet.cell_value(i,2)      
        
        id=api_sheet.cell_value(i,3)        #租车订单数字ID
        orderId=api_sheet.cell_value(i,4)
        
        ex_code = api_sheet.cell_value(i,5)
        #print ex_code
        ex_message=api_sheet.cell_value(i,6)
        
        datatemp={'uid':uid,'id':id,'orderId':orderId,\
               'token':token,'secretkey':secretkey}
        
        #print data1
        url='/order/detail'
        testcodework(datatemp, url, ex_code)
                                    
if __name__=="__main__":
    testorddetailexcel(xlsfile1)  
    
    