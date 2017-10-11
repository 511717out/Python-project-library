#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# li = [11,22,33,44,55,66,77,88,99,90]
# 需求 将所有大于66的值保存至字典的第一个key中 将小于66得的值保存至第二个key中
# 既{"k1":大于66的所有的值，"k2":小于66的所有的值}
# 第一种方法
li = [11,22,33,44,55,66,77,88,99,90]
l1 = []
l2 = []
for i in li:
    if i >= 66:
        l1.append(i)
    else:
        l2.append(i)        # append是list（列表）的方法，函数参数是可以是任意一个元素，作用是在列表的最后添加上这个新元素
temp = {"k1":l1,"k2":l2}
print(temp)

# 第二种方法
li = [11,22,33,44,55,66,77,88,99,90]
temp = {"k1":[],"k2":[]}
for i in li:
    if i >= 66:
        temp["k1"].append(i)
    else:
        temp["k2"].append(i)
print(temp)
