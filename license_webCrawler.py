
#time: 2017/09/03
#version: 3.6.1
#__author__: Haosen

import urllib.request,urllib.parse
import http.cookiejar
from json import  loads

c = http.cookiejar.LWPCookieJar()
cookie = urllib.request.HTTPCookieProcessor(c)
opener = urllib.request.build_opener(cookie)
urllib.request.install_opener(opener=opener)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Referer": "http://cx.cnca.cn/rjwcx/web/cert/publicCert.do?progId=10&title=%E8%AE%A4%E8%AF%81%E7%BB%93%E6%9E%9C%0A%09%20%20%20%20%20%20%20%20"
}


def getList():

    req = urllib.request.Request("http://cx.cnca.cn/rjwcx/web/cert/queryOrg.do?progId=10",headers=headers)

    #验证码
    with open('code.png','wb')as fn:
        fn.write(opener.open("http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1506825159502").read())
    code = input("请输入验证码：")

    data = {
        'certNumber': '',
        'orgName': '北京百度网讯科技有限公司',
        'queryType': 'public',
        'checkCode': code,
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    html = opener.open(req,data=data).read()
    result = loads(html)
    return result['data'],code

def getCertList(orgName,orgCode,checkC,code):

    req = urllib.request.Request('http://cx.cnca.cn/rjwcx/web/cert/list.do?progId=10',headers=headers)

    data = {
        'orgName':orgName,
        'orgCode':orgCode,
        'method':'queryCertByOrg',
        'needCheck':'false',
        'checkC':checkC,
        'randomCheckCode':code,
        'queryType':'public',
        'page':'1',
        'rows':'10',
        'checkCode':'',
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    html = opener.open(req,data=data).read()
    print(html)

c_List,code = getList()
for i in c_List:
    getCertList(i['orgName'],i['orgCode'],i['checkC'],code)
    break
