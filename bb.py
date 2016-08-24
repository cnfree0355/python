#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 冒泡排序"""
def bubble_sort_flag(list):
    length = len(list)
    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return list
    return list

print "冒泡排序算法"
print bubble_sort_flag([1,3,6,8,4,2,5])





