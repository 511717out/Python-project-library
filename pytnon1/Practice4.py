# _*_ coding:utf-8 _*_

"""
输出 1-100以内的和
"""
# 先输出1-100  然后再把和放到sum中
start = 1
sum = 0
while start < 101:
	print start
	sum = sum + start
	start +=1
print sum