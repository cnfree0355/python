#!/usr/bin/env python
# encoding: utf-8

import json
import urllib2
url = "http://cn.bing.com"
response = urllib2.urlopen(url)
#data = json.load(response)
print response

print "the use of loads"

url="http://news.163.com"
response = urllib2.urlopen(url)
data = json.loads(response.read())
