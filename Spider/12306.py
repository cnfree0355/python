#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 23:07
# @Author  : GHL
# @File    : 12306.py

from collections import OrderedDict
import requests
import time
import json

requests.packages.urllib3.disable_warnings()  # 关闭ssl 警告
Session_get = requests.Session()


class BuyTickets(object):
    def __init__(self, book_datetime, start_station, terminal_station, ticket_type):
        pass
        # 12306 对参数顺序严格限制
        # payload = {
        #     "purpose_codes": ticket_type,
        #     "leftTicketDTO.train_date": book_datetime,
        #     "leftTicketDTO.from_station": start_station,
        #     "leftTicketDTO.to_station": terminal_station
        # }

        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 "
                          "(KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36"
        }
        # 登录验证码接口
        code_url = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&0.321423434"
        # 余票查询url 以及参数
        # leftTicket_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?"   # 使用payload 参数会无序
        # tickets_info = Session_get.get(leftTicket_url, params=payload, verify=False).content
        original_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?"
        left_ticket_url = original_url + "leftTicketDTO.train_date=" + book_datetime + "&leftTicketDTO.from_station=" \
                          + start_station + "&leftTicketDTO.to_station=" + terminal_station + "&purpose_codes=" \
                          + ticket_type

        tickets_info = Session_get.get(left_ticket_url, verify=False, headers=headers).content
        print(tickets_info)
        # print json.loads(tickets_info, indent=10, separators=('\"', ': '), encoding="utf-8")


if __name__ == "__main__":
    BuyUser = BuyTickets('2017-01-21', 'WHN', 'SNN', 'ADULT')
