#!/usr/bin/env python
import urllib
import urllib2
#response = urllib2.urlopen('http://www.soouya.com')
request = urllib2.Request('http://www.soouya.com')
response = urllib2.urlopen(request)
html = response.read()
print html 

