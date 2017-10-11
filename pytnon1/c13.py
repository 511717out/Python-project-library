#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# list列表
# s1 = "李露"
# l1 = list(s1)   # 内部会for循环，将循环的每一个元素，当做列表的元素
# # 结果 {"李","露"}
# print(l1)
#
# # 元组转列表
# t2 = ("alex","laonanhai","seven")
# l2 = list(t2)
# print(l2)
#
# # 字典转换
# dic = {"k1":"alex","k2":"seven"}
# l3 = list(dic.items())
# print(l3)
#
# # 追加
# li =[111,22,3]
# # li.append()
# # 清除
# # li.clear()
# # 扩展自己，用另外一个可迭代对象，扩充到自己内部
# # str list dict tuple
# s = "李露"
# li.extend(s)
# print(li)
#
# # 清除空格
# # s = "alex"
# # news = s.strip()
# # print(news)
#
# # 翻转，自己内部元素翻转
# li.reverse()
#
# # 向指定位置插入指定元素
# li.insert(1,"x")
#
# # 公共功能
# # 索引
# # 切片
# # for
# # len

# 嵌套
li = ["alex","eric","weven",123]
print(li)
li = ["alex",123,{"k1":"v1","k2":{"yy":(11,22,123),"li":456}}]
print(li)
print(li[2])
print(li[2]['k2'])
print(li[2]['k2']['yy'])
print(li[2]['k2']['yy'][2])