#coding:utf-8
'''
Created on 2015��12��27��

@author: Administrator
'''
from testchangepwdxls import testchangepwdexcel
from testusergetxls import testusergetexcel
from testloginxls import testloginexcel
from testlogoutxls import testlogoutexcel
from testusergetauthxls import testusergetauthexcel
from teststationdetailxls import teststationdetexcel
from teststationnearbyxls import teststationnearbyexcel
from teststationnearbydisxls import teststationnearbydisexcel

from testuserupdatexls import testupdateexcel

from testcardetailxls import testcardetailexcel
from testcarnearbyxls import testcarnearbyexcel
from testcarpeccxls import testpeccancylistexcel
from testcargetprefee import testcargetprefeeexcel
from testorderreservexls import testorderreserveexcel
from testordersubmitxls import testordersubmitexcel
#下面三个暂时不写入测试套
from testordercancheckxls import testordercancheexcel
from testordercanclexls import testordercancleexcel
from testorderdelhisxls import testorddelhisexcel


from testorderlistxls import testorderlistexcel
from testorddetailxls import testorddetailexcel

from testinvoigetord import testinvgetordexcel
from testinvoicedel import testinvoidelexcel
from testpayprexls import testpaypreexcel

from testusercenxls import testusercenexcel
from testwalhoxls import testwallhomeexcel
from testwaldayxls import testwaldaybookexcel

from testmisgetareaxls import testmisgetarea
import json
import httplib, urllib
import time
import login
import xlrd
import sys
from testbaseurl import *
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":

    try:
        
        testchangepwdexcel()
        testusergetauthexcel()
        testusergetexcel()
        testupdateexcel()
        
        teststationdetexcel()
        teststationnearbyexcel()
        teststationnearbydisexcel()
        
        testcardetailexcel()
        testcarnearbyexcel()
        testpeccancylistexcel()
        testcargetprefeeexcel()
        testorderreserveexcel()
        testordersubmitexcel()
        
        testpaypreexcel()
        #下面三个不写入测试套,testorddetailexcel()除外
        testordercancheexcel()
        testordercancleexcel()
        testorddetailexcel()
        testorddelhisexcel()
        
        testorderlistexcel()
        
        
        testinvgetordexcel()
        
        #不写入测试套
        #testinvoidelexcel()
        
        
        testusercenexcel()
        testwallhomeexcel()
        
        testwaldaybookexcel()
        testmisgetarea()
        #login会修改token，放在最后
        testlogoutexcel()
        testloginexcel()
    except Exception, e:
        print e