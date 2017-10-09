#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 字典的每一个元素都是一个键值对
user_info = {
    "name":"alex",
    "age":73,
    "gender":'m'
}

# 索引
print(user_info["name"])

# 切片
# 没有办法切片

# 循环  默认只输出key
for i in user_info:
    print(i)


print(user_info.keys())     # 获取字典所有的key键
print(user_info.values())       # 获取所有的值
print(user_info.items())        # 获取所有的键值对

# 循环所有的键
for i in user_info.keys():
    print(i)

# 循环所有的值
for i in user_info.values():
    print(i)

# 循环所有的键值对
for k,i in user_info.items():
    print(k,i)

# clear,清除所有内容
# user_info.clear()
# print(user_info)

# gie 根据key获取值，如果key不存在可以指定一个默认值
val = user_info.get('age')
print(val)
val = user_info.get('age111','123')       # 没有age111这个键,后面值自己给就像123
print(val)

# 索引取值时，key不存在报错
# print(user_info['age'])
# print(user_info['age111'])

# has_key 检查字典中指定key是否存在 3.0没有了
# 可以用in 代替
ret = 'age' in user_info.keys()
print(ret)

# update 批量更新
tast = {
    "a1":123,
    "a2":456,
}
user_info.update(tast)
print(user_info)

# del 删除指定索引的键值对
del user_info['a1']
print(user_info)