#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 列表
name_list = ["eirc","alex","tony","seven"]
# 索引
print(name_list[0])
# 切片
print(name_list[0:2])
# print(name_list[2:len(name_list)])
# for循环
for i in name_list:
    print(i)


# 列表内部提供的其他功能
# append 后追加
name_list.append('seyen')
name_list.append('seyen')
name_list.append('seyen')
print(name_list)
print(name_list.count('seyen'))         # 元素出现的次数
# iterable,可迭代的
temp = [11,22,33,45,]
name_list.extend(temp)
print(name_list)
print(name_list.index('alex'))      # 获取指定元素的索引位子
print(name_list.insert(1,'Sb'))     # 表示往某个索引位子插一个值
a1 = name_list.pop()                # 在列表中移除最后一个值并赋值给a1
print(a1)
name_list.remove('seven')           # 移除某个元素 默认从左往右只移除一个
print(name_list)
name_list.reverse()                 # 把列表倒过来了
print(name_list)

# 删除指定索引位子  也可以切片删除
print(name_list)
del name_list[1]
print(name_list)