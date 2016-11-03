#!/bin/env python
# coding=utf-8


import requests

url = 'http://testoms.soouya.com/crm/cm/Seed/login.do'
HEADERS = {
    "User-Agent": "Chrome/52.0.2743.82 Safari/537.36"
}
# 设置同一session 来访问
s = requests.Session()
login_info = {"userName": "admin", "pwd": "cc03e747a6afbbcbf8be7668acfebee5"}
r = s.post(url, data=login_info, headers=HEADERS)  # data 传递post 请求内容
pay_load = {"pageNumber": 5,
            "pageSize": 30,
            "status": 0}
# parms 拼接请求
v = s.get('http://testoms.soouya.com/crm/cm/Seed/getSeedPage.do', params=pay_load)
res = v.content
print res
