# _*_ coding:utf-8 _*_

"""
输出1-100内的所有奇数
"""
# 先输出1-100以内的数
#只显示奇数

temp = 1
sum = 0
while temp<101:
	time = temp % 2
	if time == 1:
		print temp
		sum = sum + temp
	else: 
		pass
	temp += 1

print sum
		