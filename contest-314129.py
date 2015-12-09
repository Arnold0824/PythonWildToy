import urllib
import urllib.parse
import sys
import http.cookiejar

#you can change DATA to get whatever you what
def test():
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())# add cookie to prentend
    headers = [('Host', 'img0.imgtn.bdimg.com'),  # add header to pretend to be a explore
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
            ('X-Forwarded-For', '219.78.113.243'),
            ('If-Modified-Since', 'Thu, 01 Jan 1970 00:00:00 GMT')]

    opener.addheaders = headers
    try:
        url = 'https://elibrary.ferc.gov/IDMWS/search/results.asp'
        data={'FROMdt':'','TOdt':'','firstDt':'1/1/1904','LastDt':'12/31/2037','DocsStart':'0','DocsLimit':'200','SortSpec':'filed_date desc accession_num asc','datefield':'filed_date','date':'between','dFROM':'11/09/2015','dTO':'12/09/2015','dYEAR':'1','dMONTH':'1','dDAY':'1','NotCategories':'submittal,issuance','category':'submittal','category':'issuance','libraryall':'electric, hydro, gas, rulemaking, oil, general','docket':'','subdock_radio':'all_subdockets','subdocket':'','class':'999','type':'999','textsearch':'','description':'description','fulltext':'fulltext','DocsCount':'50'}
        data=urllib.parse.urlencode(data).encode('utf-8')
        j=opener.open(url,data).read()
        print(str(data,encoding='utf-8')+'\nOK--------------\n'+str(j,encoding='utf-8'))#print test data
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))

if __name__ == '__main__':
    test()#have a try
