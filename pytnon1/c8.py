#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# li = ["alex","eric"]    # 列表
# li = ("alex","eric")    # 元祖
# s = "_".join(li)        # .join 把字符串链接起来
# print(s)


# s = "alex"
# # news = s.lstrip()       # 移除左边空白‘
# news = s.rstrip()       # 移除右边空白
# news = s.strip()        # 移除两边空白
# print(news)


# s = "alex SB alex"
# ret = s.partition("SB")     # 其他先不知道 搞成元祖类型了
# print(ret)


# s = "alex SB alex"
# ret = s.replace("al","BB",1)        # 你想把谁替换成谁  加后面参数从左往右找几个
# print(ret)

# s = "alexalex"
# ret = s.split("e",1)        # 分割
# print(ret)
#
# s = "aLeX"
# print(s.swapcase())         # 大写遍小写  小写变大写
#
# s = "the school"
# ret = s.title()         # 变标题
# print(ret)
#
#
# # 字符串索引
# s = "alex"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# ret = len(s)
# print(ret)          # 知道这个字符串有多长

# 切片
s = "alex"
# 0<=  <2
# print(s[0:2])

# 循环
# start = 0
# while start < len(s):
#     temp = s[start]
#     print(temp)
#     start += 1

# for 循环
for item in s:          # item 随便定义的
    if item == "L":
        break
    print(item)
