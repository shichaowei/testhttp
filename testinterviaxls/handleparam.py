#coding:utf-8
'''
Created on 2015��12��16��

@author: Administrator
'''
import time
import copy

def removeparam(datatemp):
    temp=[]
    keytemp=[]
    tempdic={}
    flag=0
    for key in datatemp.keys():
        #print key
        #print len(datatemp)
        if flag<len(datatemp):
            tempdic=copy.copy(datatemp)
            del tempdic[key]
            #print tempdic
            temp.append(tempdic)
            keytemp.append(key)
            flag+=1
    return temp,keytemp


def addsomeparam(datatemp):
    
    addkey='addtestparam'
    tempdic=copy.copy(datatemp)
    tempdic[addkey]='12345魏士超'
    return tempdic


def overlengthparam(datatemp,exparamlist=[]):
    temp=[]
    tempdic={}
    flag=0
    for key in datatemp.keys():
        print key
        print len(datatemp)
        if flag<len(datatemp) and exparamlist.count(key)==0:
            tempdic=copy.copy(datatemp)
            tempdic[key]='weishichao魏士超222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222'
            print tempdic
            temp.append(tempdic)
            flag+=1
    return temp



'''            
if __name__=="__main__":
    testtakeTime=long(time.time()*1000+5*60*1000)
    testreturnTime=long(testtakeTime+2*3600*1000)
    carId=1081           #车辆id
    rentType=1
    takeTime=testtakeTime
    returnTime=testreturnTime
    takeStationId=1001
    returnStationId=1001
    exInsuranceTag=0
    uid=123
    token=456
    secretkey='12345678'
    
    datatemp={'carId':carId,'rentType':rentType,\
                          'takeTime':takeTime,'returnTime':returnTime,\
                          'takeStationId':takeStationId,'returnStationId':returnStationId,\
                          'exInsuranceTag':exInsuranceTag,\
                          'uid':uid,'token':token,'secretkey':secretkey}  
    #del datatemp['secretkey']
    #print datatemp
    print overlengthparam(datatemp, exparamlist=['cardId','uid'])
    
 '''   