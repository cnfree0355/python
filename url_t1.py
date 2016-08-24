#!/bin/env python
import urllib
import urllib2
url = 'http://oms.soouya.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = dict(username='cqc', password="XXXX")
headers = {'User-Agent': user_agent}
data = urllib.url.encode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

