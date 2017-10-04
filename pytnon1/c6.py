#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 基本数据类型常用的功能：
# 1，整数， int

n1 = 123
n2 = 456
print(n1 + n2)
# 这两个功能是一样的
print(n1.__add__(n2))

# 获取可表示的二进制最短位数
n1 = 4      # 二进制的4表示为00000100
ret = n1.bit_length()
print(ret)