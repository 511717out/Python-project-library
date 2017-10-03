#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 查看字符串"SB"在不在字符串"Alex SB"里面
s = "Alex SB"
ret = "SB" in s
print(ret)

# in如果在指定的序列中找到值返回True,否则返回False
li = ['alex','eric','rain']
ret = "alex" in li
print(ret)

# not in 如果在指定的列表中没有找到值返回True，否则返回False
li = ['alex','eric','eain']
ret = "alex" not in li
print(ret)