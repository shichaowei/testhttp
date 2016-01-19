#coding:utf-8
'''
Created on 2015��12��27��

@author: Administrator
'''
import json
import httplib, urllib
import time
import logging
from handleparam import removeparam,addsomeparam

false='False'
true='True'
null=''
logging.basicConfig(encode="utf-8",\
                    level=logging.DEBUG,\
            #format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',\
            format='%(asctime)s [line:%(lineno)d] %(message)s',\
            datefmt='%a, %d %b %Y %H:%M:%S',\
            filename='myapp.log',\
            filemode='w')

def printtitle(title):
    print title
    logging.debug('\n')
    logging.debug(title)

def printandlog(datatemp):
    print datatemp
    #logging.debug('\n')
    logging.debug(datatemp)   



def urlpost(datatemp,url):
    #logging.debug(u'post parameter is')
    logging.debug('ulr parameter is'+url)
    global false
    global true
    global null
    data_string = json.dumps(datatemp)
    logging.debug(data_string)
    httpClient = None
    try:
        '''
        params = urllib.urlencode({'name': 'tom', 'age': 22})
        print params
        '''
        headers = {"Content-type": "application/json"
                        , "Accept": "application/json"}
     
        httpClient = httplib.HTTPConnection("192.168.1.251", 5000, timeout=30)
        httpClient.request("POST", url, data_string, headers)
     
        response = httpClient.getresponse()
        resulttemp=response.read()
        logging.debug(resulttemp)
        #print resulttemp
        return eval(resulttemp)
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
            
def testcodework(datatemp,url,ex_code):
    flag='Failed'
    #print datatemp
    resulttemp=urlpost(datatemp,url)
    #print resulttemp
    
    #print resulttemp['resultCode']
    if str(resulttemp['resultCode'])==ex_code:
        printandlog('test code=%s pass'%ex_code)
        falg='PASS'
    else:
        printandlog('test code=%s failed'%ex_code) 
          
    if ex_code=='200':
        ##测试表单中缺少某个字段
        printandlog('START less parameter AND add  parameter')
        temp,keytemp=removeparam(datatemp)
        #print keytemp
        for (flag,key) in zip(temp,keytemp):
            #print flag
            resulttemp=urlpost(flag,url)
            #print key
            if str(resulttemp['resultCode'])=='200' and key!='distance' and key!='offset' \
                and key!='priceRange' and key!='brand' and key!='models' and key!='sorts'\
                and key!='status' and  key!='exInsuranceTag' and key!='upic' and key!='orderId':
                printandlog('test less parameter failed,param lack %s response is 200'%key)
            else:
                pass

        '''
        #测试表单中含有多余字段
        addparatemp=addsomeparam(datatemp)
        resulttemp=urlpost(addparatemp,url)
        #print key
        if str(resulttemp['resultCode'])=='200':
            pass
        else:
            printandlog('test add parameter failed,param is')
            printandlog(addparatemp)
        '''
        printandlog('FINISH less parameter AND add  parameter')    
        
           
    return flag    