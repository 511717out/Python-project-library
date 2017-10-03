#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# range,xrange
# py2.7
# range,用获取指定范围内的数，range(0,10000)
# xrange,用获取指定范围内的数，xrange(0,10000)
# for i in xrange(1,10000):
#      print(i)


# py3,range,等同于xrange
#  print(range(1,10))     # 2.7中会直接创建，3.5中不会创建 需要for循环
# for i in range(1,10):
#     print(i)

# for i in range(1,10,2):     # 2是中间间隔的值
#     print(i)
#
# for i in range(10,1,-1):        # ????
#     print(i)

li = ["alex", "eirc"]

leee = len(li)

for i in range(0,leee):
    print(i,li[i])