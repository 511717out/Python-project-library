#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# a1 = "alex"
# ret = a1.capitalize()       # 方法的功能是让字符串首字母大写
# print(ret)

# a1 = "alex"
# ret = a1.center(20,'_')         # 内容居中 定义总长度 空白处填充内容
# print(ret)

# a1 = "alex is alph"
# ret = a1.count("al")            # 查找子序列出现的个数
# ret = a1.count("al",0,10)       # 从第0个字符串开始查找到第10个字符串结束
# print(ret)

# temp = "hello"
# # 获取字符串里大于等于零的位子，小于2的位子
# print(temp.endswith('e',0,2))       # 是否以XXXX结尾

# centent = "hello\t999"      # \t 制表符  代表的是一个tab键
# print(centent)
# print(centent.expandtabs())     # 默认是8个空格
# print(centent.expandtabs(20))   # 20个空格

# s = "alex hello"
# print(s.find('l'))      # 寻找子序列的位子，如果没找到返回-1

s = "hello {0}, age {1}"
print(s)
# {0} 占位符
new = s.format('alex',19)       # 字符串格式化
print(new)