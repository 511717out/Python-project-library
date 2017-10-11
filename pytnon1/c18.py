#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 总资产
asset_all = 0
li = input("请输入总资产：")
asset_all = int(li)

goods = [
    {"name":"电脑","price":1999},
    {"name":"鼠标","price":10},
    {"name":"游艇","price":20},
    {"name":"美女","price":998},
]
for i in goods:
    # {"name":"电脑","price":1998}
    print(i["name"],i["price"])
car_dict = {}
# car_dict = {
#           "电脑":{"price":单价，num:123}
# }
while True:
    i2 = input("请选择商品(Y/y结算)：")    # 电脑
    if i2.lower() == "y":
        break
    # 循环所有的商品，查找需要的商品
    for item in goods:
        if item["name"] == i2:
            # item = {"name":"电脑","prite":1999}
            name = item["name"]
            # 判断购物车是否已经有该商品，有，num+1
            if name in car_dict.keys():
                # pass
                car_dict[name]["num"] = car_dict[name]["num"] + 1
            else:
                car_dict[name] = {"num":1,"single_price":item["price"]}
print(car_dict)
# {
#       "鼠标": {"single_price":10,"num":1}, 1*10
#       "电脑": {"single_price":1999,"num":9} 9*1999
# }
all_price = 0
for k,v in car_dict.items():
    n = v["single_price"]
    m = v["num"]
    all_sum = m * n
    all_price = all_price + all_sum

if all_price > asset_all:
    print("穷逼")
else:
    print("我跟你回家吧")

