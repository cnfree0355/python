#!/bin/bash
for i  in `ls *.py`
  do
    if  [ ! -x $i ];then
    echo -e "\033[34m  $i 为不可执行文件，现在加上可执行权限\033[0m"  
    chmod u+x $i
    fi
done
