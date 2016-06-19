#!/usr/bin/env python
# encoding: utf-8
def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print reversed_cmp(35,52)
print sorted([36,5,12,9,18],reversed_cmp)

print "降序排列"
print sorted([36, 5, 12, 9, 21], lambda x, y: y - x)
print "巧妙用法"
print sorted([36, 5, 12, 9, 21])[::-1]


