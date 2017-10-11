#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 去除空格并输出以a开头c结尾的所有的元素
li = ("alec","aric","Alee","Tony","rain")
for i in li:
    new_i = i.strip()   # strip()去除空格
    if (new_i.startswith("a") or new_i.startswith("A")) and new_i.endswith("c"):
        # startswith 查找以什么什么开头，endswith()查找以什么什么结尾
        print(new_i)