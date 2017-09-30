# _*_ coding:utf-8 _*_
# 编码

# py2
temp = "李杰" # utf-8
# 解码，需要指定原来是什么编码
temp_unicode = temp.decode('utf-8')
# 编码，需要需要指定要编成什么码
temp_gbk = temp_unicode.encode('gbk')
print(temp_gbk)
