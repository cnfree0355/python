#!/usr/bin/env python
# encoding: utf-8
import os
print os.environ
print os.getenv('PATH')

print os.path.abspath('.')
print os.path.join('/root/','/python1')
#os.mkdir('/root/guo/pytest')
#os.rmdir('/root/guo/pytest')
print '*'*20
print '合并拆分并不要求目录文件真实存在,只对字符串操作'
print '拆分路劲,最后一部分是最后级别目录或者文件'
print os.path.split('/etc/mysql/my.cnf')
print '获取文件扩展名'
print os.path.splitext('/root/python/file/text.txt')
