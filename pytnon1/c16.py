#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 输出商品列表，用户输入序号，选中用户选中的商品
# 商品 li = ["手机","电脑","鼠标垫","游艇"]
li = ["手机","电脑","鼠标垫","游艇"]
for i,j in enumerate(li):
    print(i+1,j)
num = input("请输入序列号：")
num = int(num)
len_li = len(li)
if num > 0 and num<=len_li:
    print(li[num-1])
else:
    print("商品不存在！")