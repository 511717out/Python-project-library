# _*_ coding:utf-8 _*_


"""
用户登录（三次机会重试）
"""

i = 0
while i < 3:
	user = raw_input("username:")
	pwd = raw_input("password:")
	if user == "alex" and pwd == "123":
		print ("yes")
		break
	else :
	 print ("no")
	i += 1
	 