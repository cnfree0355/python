#!/usr/bin/env python
# encoding: utf-8
import os
print [x for x in os.listdir('.') if os.path.isdir(x)]

print '输出当前路径下的py文件'
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] =='.py' ]


