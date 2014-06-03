#@author Zhanglin
# -*- coding: GB2312 -*-
import mechanize
import cookielib
import time
import urllib
import re
import string

def search(i):
    # Browser
    br = mechanize.Browser()
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # Browser options
    br.set_handle_equiv(True)
    #br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open('http://google.com')
    reResult = re.compile("\d+? result")
    data = {'q' : i}
    q = urllib.urlencode(data)
    print q
    #print 'https://www.google.com/search?hl=en&gl=us&tbm=nws&authuser=0&tbs=qdr:h72&'+q
    html = ""
    r = br.open('https://www.google.com/search?hl=en&gl=us&tbm=nws&authuser=0&tbs=qdr:h72&'+q)
    time.sleep(1)
    html = r.read()
    #print "Error: ",q
    #print html
    y = reResult.search(html)
    #print "group=",y.group()
    x = ""
    if y != None:
        x = y.group()[:-6]
    else:
        x = "0"
    print "company=",i," results=",x


dataName = "list.txt"
f = file(dataName,"r")
page = f.read()
f.close()

list = page.split("\n")
print list
for i in list:
    search(i)

'''

# Browser
br = mechanize.Browser()
# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)
# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# Open some site, let's pick a random one, the first that pops in mind:
br.open('http://google.com')

resultName = time.strftime("%m%d%Y")+".txt"
fileResult = file(resultName,"w")

print time.strftime("%m%d%Y")

reResult = re.compile("\d+? result")
for i in list:
    data = {'q' : i}
    q = urllib.urlencode(data)
    print q
    #print 'https://www.google.com/search?hl=en&gl=us&tbm=nws&authuser=0&tbs=qdr:h72&'+q
    html = ""
    r = br.open('https://www.google.com/search?hl=en&gl=us&tbm=nws&authuser=0&tbs=qdr:h72&'+q)
    time.sleep(1)
    html = r.read()
    #print "Error: ",q
    #print html
    y = reResult.search(html)
    #print "group=",y.group()
    x = ""
    if y != None:
        x = y.group()[:-6]
    else:
        x = "0"
    print "company=",i," results=",x
    fileResult.write(i+"\t")
    fileResult.write(str(string.atoi(x)))
    fileResult.write("\n")

fileResult.close()
'''
print "ok"