# -*- coding:utf-8 -*-

print('hello,python')
print('hello,'+'python')
temp = '你是我的小苹果'
temp_unicode = temp.decode('utf-8')
temp_gbk = temp_unicode.encode("gbk")
print(temp_gbk)