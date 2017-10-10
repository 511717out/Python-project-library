#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# int两种创建方式  等同一样
# int 类型不够自动变成long
# a = 123
# a => int => _init_(123)
# a = int(123)
# a2 = 123
# a3 = 123
# print(a)
#
# a1 = int("0b100",2)
# print(a1)

# str 字符串中特有的功能
s1 = "alex"
# 无参数，创建空字符串
# 一个参数，创建普通字符串
# 两个参数，int(字节，编码)

# 两端去除空格
# s1.strip()

# 以...开头
# s1.startswith()

# 找子序列 "12","h"
# s1.find()

# 将字符串中的某子序列替换成指定的值
# s1.replace()

# 变大写
# s1.upper()

# 是什么什么吗？
#  s1.isalpha()

# 公共功能
# 索引：只能取一个元素
# 切片：取多个元素
# len:
# for:
# 编码for:
name = "李露"
for i in name:
    print(i)
    bytes_list = bytes(i,encoding="utf-8")      # bytes可以将字符串转换成字节
    print(bytes_list)           # 默认每一个字节都是十六进制表示
    for b in bytes_list:        # 默认每一个字节都是十进制表示
        print(b)
# 3.5 for循环的时候，循环的每一个元素是字符
# 字符 =》 字节
bytes_list = bytes("字符串",encoding="utf-8")

# utf-8 -> 3字节
# gbk   -> 2字节


# a = "李露"
# # 将字符转换成字节
# b1 = bytes(a,encoding='utf-8')      # 6个字节
# print(b1)
# b2 = bytes(a,encoding='gbk')        # 4个字节
# print(b2)
#
# # 将字节转换成字符串
#
# newa1 = str(b1,encoding="utf-8")
# print(newa1)
#
# newa2 = str(b2,encoding="gbk")
# print(newa2)
#
# x = str()
# # 要么是创建字符串
# # 要么是转换成字符串
#
# m = bytes()
# # 创建字节
# # 转换成字节，字符串，要编程什么编码类型的字节
# 10进制的数字 =》2进制
# bin(10进制数字)
