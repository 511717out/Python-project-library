#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 用户交互，显示省市县三级联动的选择
dic = {
    "河北" : {
        "石家庄" : ["鹿泉","运城","元氏"],
        "邯郸" : ["永年","涉县","赤县"],
    },
    "河南" : {
    "郑州" : ["不知道","少林寺","嵩山"],
    "开封" : ["包拯","展昭","威士忌"],
    },
    "山西" : {
        "太原" : ["xxx","ooo","wwww"],
        "远程" : ["aaa","sss","ccc0"],
    }
}
# 循环输出所有的省
for x in dic:
    print(x)

li = input("请输出省份:")
a = dic[li]

# 循环输出所有的市
for j in a:
    print(j)
l2 = input("请输入市：")
b = dic[li][l2]     # 先取出市 再从市里取值
print(b)
