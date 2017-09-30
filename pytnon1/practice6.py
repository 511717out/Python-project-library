# _*_ coding:utf-8 _*_

"""
输出1-100以内的偶数
并求和
"""

temp = 1
sum = 0
while temp < 101:
	time = temp % 2 
	if time == 0:
		print temp
		sum = sum + temp
	else:
		pass
		# temp += 1  注意
	temp += 1
print sum