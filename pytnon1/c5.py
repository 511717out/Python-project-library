#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 查看对象的类，或对象所具备的功能


# 通过type找到它是什么类
temp = "hey"
# 通过type获取字符串类型
chengbao = type(temp)
print(chengbao)
temp.upper()    # 变大写
temp.lower()    # 变小写
# str,ctrl+鼠标左找到str的类，内部所有的方法


# dir
temp = "alex"
b = dir(temp)


# help, type
help(type(temp))