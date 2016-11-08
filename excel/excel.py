#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/4 16:15
# @Author  : GHL
# @File    : excel.py


from xlrd import open_workbook
# 写入excel 仅支持xls格式
# from xlwt import Workbook
# 下面模块用了写入已经存在的excel 文件
from xlutils.copy import copy

# 也可以用下面这个模块更简单高效
# import openpyxl

# 打开excel 文件
file_name = "ab.xls"
data = open_workbook(file_name)
wb = copy(data)
s = wb.get_sheet(0)

# 获取工作表名称
# print data.sheet_names()[0]
# 获取sheet工作表
table = data.sheet_by_name(u'交易明细')
table2 = data.sheet_by_name(u"Sheet2")
# 获取行数和列数
rows = table.nrows
rows2 = table2.nrows


def show_row_values(num):
    for n in range(1, num):
        company_values = table.row_values(n)[0]
        yield company_values


def show_sheet2_values(row_num):
    for i in range(1, row_num):
        sheet2_values = table2.row_values(i)[:]
        yield sheet2_values


li = show_row_values(rows)
li2 = show_sheet2_values(rows2)

# 将li2 组装成一个dict
res = {k: v for k, v in li2}

for index, name in zip(range(1, rows), li):
    value = res[name]
    # print index,name
    s.write(index, 3, value)
# 保存文件
wb.save(file_name)

# 获取每个单元格的数值,都以0 开头其中(0,0)表示第一行第一列
# cell_b2 = table.cell(1, 1).value
# 如果是日期格式需要xldate 函数
# show_date = xlrd.xldate_as_tuple(cell_b2, data.datemode)
# print show_date

# 分别使用行列索引
# cell_A1 = table.row(1)[0].value
# print cell_A1
