import urllib
import urllib.parse
import sys
import http.cookiejar
import random
import time
import socket


def test(b, opener):
    try:
        url = "http://s1.eqxiu.com/eqs/page/23377355?1=1&eqrcode=1&from=timeline&isappinstalled=0&ad=1&time=" + str(b)
        opener.open(url)
        socket.setdefaulttimeout(1)
        print('-Ok------------')
    except:
        print('链接断开了,重来')


def go():
       
    su=1
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    for x in range(0,int(input('请输入次数:'))):
        try:
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
               ('If-None-Match', '90101f651aa74454922de2ad74'),
               ('Referer',
                'http://viewer.maka.im/pcviewer/5SXPZNHN'),
               ('X-Forwarded-For','219.78.113.243'),
               ('If-Modified-Since', 'Thu, 01 Jan 1970 00:00:00 GMT')]
            opener.addheaders = headers
            test(b,opener)
            print('这是第'+str(su)+'次刷票.')
            su+=1
        except:
            print('产生随机数失败')
            continue

if __name__ == '__main__':
    go()
