import urllib
import urllib.parse
import sys
import http.cookiejar
import random
import time
import socket
import uuid

def test(taID,a, b,opener):
    u=str(uuid.uuid1())
    try:       
        url = "http://tongji.datastory.com.cn/visit.gif?url=http%3A%2F%2Fviewer.maka.im%2Fk%2F"+taID+"&taskId=maka-"+taID+"&referer=http%3A%2F%2Fviewer.maka.im%2Fpcviewer%2F5SXPZNHN&screen=2560x1440&fromType=0&dsId="+u+"&timestampId=" + \
        str(b) + "&fromDsId="+u+"&fromTimestamp=&channelId=&rnd=" + str(a)
        opener.open(url)
        socket.setdefaulttimeout(2)
        print('OK--------------')
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))

def go():
       
    su=1
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    url=input('请输入作品的地址后8位(作品ID):')

    for x in range(0,int(input('请输入次数:'))):
        try:
            a = random.randint(1000000, 9999999)
            b = round(time.time())
            headers = [('Host', 'img0.imgtn.bdimg.com'),#加上header才能以假乱真
               ('Connection', 'none'),
               ('Cache-Control', 'max-age=0'),
               ('Accept',
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
               ('User-Agent',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'),
               ('Accept-Encoding', 'gzip,deflate,sdch'),
               ('Accept-Language', 'zh-CN,zh;q=0.8'),
               ('If-None-Match', '90101f'+str(a)+'651aa74454922de2ad74'),
               ('Referer',
                'http://viewer.maka.im/pcviewer/5SXPZNHN'),
               ('X-Forwarded-For','219.78.113.243'),
               ('If-Modified-Since', 'Thu, 01 Jan 1970 00:00:00 GMT')]
            opener.addheaders = headers
            test(url,a,b,opener)
            print('这是第'+str(su)+'次刷票.')
            su+=1
            #time.sleep(0.1)
        except:
            print('产生随机数失败')
            continue

if __name__ == '__main__':
    go()

    
