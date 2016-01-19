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
from testbaseurl import printtitle,printandlog
from testbaseurl import *
import logging

xlsfile1 = r'F:/testexcel/testcarcontrol.xls'
reload(sys)
sys.setdefaultencoding('utf-8')



def testchangepwdexcel(xlsfile=xlsfile1):
    printtitle('START CHANGPWD')
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        uid = api_sheet.cell_value(i,0)   # �ֱ��������е�client_id��password��sign��ex_code
        #print mobile
        token = api_sheet.cell_value(i,1)
        #print password
        secretkey = api_sheet.cell_value(i,2)
        carId=api_sheet.cell_value(i,3)
        type = api_sheet.cell_value(i,4)
        latitude=api_sheet.cell_value(i,5)
        longitude=api_sheet.cell_value(i,6)
        
        ex_code=api_sheet.cell_value(i,7)
        ex_message=api_sheet.cell_value(i,8)
        #print ex_message
        #print newpwd
        
        datatemp={'latitude':latitude,'longitude':longitude,'uid':uid,'token':token,'secretkey':secretkey,\
                  'type':type,'carId':carId}
        #print data1
        url='/car/control'
        testcodework(datatemp, url, ex_code)
        
                        
if __name__=="__main__":
    testchangepwdexcel(xlsfile1)
    