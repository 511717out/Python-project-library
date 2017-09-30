# _*_ coding:utf-8 _*_

"""
求1-2+3-4+5....99所有数的和
偶数减  奇数加
"""


temp = 1
sum = 0
while temp < 100:
	time = temp % 2
	if time == 0:
		print temp
		sum = sum - temp
	else:
		print temp
		sum = sum + temp
	temp += 1
print sum



