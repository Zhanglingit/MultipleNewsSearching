#! /usr/bin/env python
#coding=utf-8

import google
import urllib
import re
import string
import time
#from urllib2 import Request, urlopen
'''
def get_page(url):
    """
    Request the given URL and return the response page, using the cookie jar.

    @type  url: str
    @param url: URL to retrieve.

    @rtype:  str
    @return: Web page retrieved for the given URL.

    @raise IOError: An exception is raised on error.
    @raise urllib2.URLError: An exception is raised on error.
    @raise urllib2.HTTPError: An exception is raised on error.
    """
    request = Request(url)
    request.add_header('User-Agent',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
    cookie_jar.add_cookie_header(request)
    response = urlopen(request)
    cookie_jar.extract_cookies(response, request)
    html = response.read()
    response.close()
    cookie_jar.save()
    return html
'''
def getCompanyList(fileName):
    f = file(fileName,"r")
    page = f.read()
    list = page.split("\n")
    f.close()
    list.remove("")
    return list

def myNewsSearch(key):
    data = {'q' : key}
    url = 'https://www.google.com/search?hl=en&gl=us&tbm=nws&authuser=0&tbs=qdr:h72&'+urllib.urlencode(data)
    page = google.get_page(url)
    return page

def countResult(page):
    '''
    reResult = re.compile("\d+? result")
    result = reResult.search(page)
    strResult = ""
    if result != None:
        strResult = result.group()
        strResult = strResult[:-6]
    else:
        strResult = "0"
    return string.atoi(strResult)
    '''
    if page.find("<div class=\"sd\" id=\"resultStats\">")==-1:
        return "Abort 0 results"
    else:
        x = page[page.find("<div class=\"sd\" id=\"resultStats\">")+33:]
        x = x[:x.find("<")]
        return x

def pageSaver(page, fileName):
    f = file(fileName,"w")
    f.write(page)
    f.close()

def resultContinue(list):
    resultName = time.strftime("%m%d%Y")+".txt"
    page = ""
    try:
        f = file(resultName, "r")
    except:
        return list
    page = f.read()
    l2 = page.split("\n")
    for i in l2:
        x = i[:i.find("\t")]
        try:
            list.remove(x)
        except:
            break
    return list


if __name__ == "__main__":
    list = getCompanyList("list.txt")
    list = resultContinue(list)
    print len(list)

    resultName = time.strftime("%m%d%Y")+".txt"
    f = file(resultName, "a")
    for i in list:
        print i,
        page = myNewsSearch(i)
        #pageSaver(page, i[:5]+".html")
        time.sleep(20)
        print countResult(page)
        f.write(i+"\t"+countResult(page)+"\n")
    f.close()






