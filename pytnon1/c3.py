#!/usr/bin/env python
# _*_ coding:utf-8 _*_

li = ["电脑", "鼠标垫", "U盘", "游艇"]
# enumerate自动生成一列，默认0自增1
for key, item in enumerate(li, 1):
    print(key, item)      # 在2.7中不会打印
# 注意input接收到值的类型为字符串
inp = input("请输入商品:")   # input2.7中不能使用
# 字符串转换成int
inp_num = int(inp)
print(li[inp_num-1])


li = ["电脑", "鼠标垫", "U盘", "游艇"]
inp = input("请输入内容:")
ret = li.index(inp)         # 根据名称搜索索引号
print(ret)
