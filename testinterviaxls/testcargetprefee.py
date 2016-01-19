#coding:utf-8
'''
Created on 2015 12 28
5.16    获取租车预估费用接口
@author: weishichao
'''

import json
from testbaseurl import *
import httplib, urllib
import time
import xlrd
import sys
import logging

xlsfile1 = r'F:/testexcel/testcargetprefee.xls'
reload(sys)
sys.setdefaultencoding('utf-8')

    
def testcargetprefeeexcel(xlsfile=xlsfile1):
     
    title='START TESTcargetprefeexcel'
    printtitle(title)
    
    book = xlrd.open_workbook(xlsfile)
    api_sheet = book.sheet_by_index(0)
    nrows = api_sheet.nrows
    
    for i in range(1,nrows):
        id = api_sheet.cell_value(i,0)   # 分别迭代表格中的client_id，password，sign和ex_code
        #print mobile
        rentType = api_sheet.cell_value(i,1)
        #print password
        takeTime = api_sheet.cell_value(i,2)
        returnTime= api_sheet.cell_value(i,3)
        uid= api_sheet.cell_value(i,4)
        token= api_sheet.cell_value(i,5)
        secretkey = api_sheet.cell_value(i,6)
        
        ex_code = api_sheet.cell_value(i,7)
        if ex_code=='200':
            takeTime=long(time.time()*1000+15*60*1000)
            returnTime=long(takeTime+2*3600*1000)
        elif ex_code=='214':
            takeTime=long(time.time()*1000-3600*1000)
            returnTime=long(time.time()*1000+2*3600*1000)
        elif ex_code=='215':
            takeTime=long(time.time()*1000+2*3600*1000)
            returnTime=long(time.time()*1000+3*3600*1000)
        elif ex_code=='216':
            takeTime=long(time.time()*1000+5*60*1000)
            returnTime=long(time.time()*1000)
        elif ex_code=='211':
            returnTime=long(time.time()*1000+2*3600*1000)
        elif ex_code=='212':
            takeTime=long(time.time()*1000-3600*1000)
        elif ex_code=='411':
            takeTime=long(time.time()*1000+5*60*1000)
            returnTime=long(takeTime+5*60*1000)
        elif ex_code=='412' and rentType=='1':
            takeTime=long(time.time()*1000+5*60*1000)
            returnTime=long(takeTime+24*3600*1000)
        elif ex_code=='412' and rentType=='2':
            takeTime=long(time.time()*1000+5*60*1000)
            returnTime=long(takeTime+4*3600*1000)
        else:
            takeTime=long(time.time()*1000+15*60*1000)
            returnTime=long(takeTime+2*3600*1000)
        #print ex_code
        ex_message=api_sheet.cell_value(i,8)
        #print ex_message
        
        datatemp={'id':id,'rentType':rentType,\
              'takeTime':takeTime,'returnTime':returnTime,'uid':uid,'token':token,\
              'secretkey':secretkey}  
        #print datatemp
        #print data1
        url='/car/getprefee'

        testcodework(datatemp, url, ex_code)
                        
if __name__=="__main__":
    testcargetprefeeexcel(xlsfile1)
    