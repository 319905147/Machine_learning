# 字典 dict 定义 使用{}来定义 ,是有键值对来组成(key-value)
# 变量 = {key1:value1, key2:value2, ......}  一个键值对是一个元素
# 字典的key 一般是 字符串和数字类型(int   ,   float)  不能是    列表
# value 可以是任何类型


# 定义 空字典
my_dict = {}
my_dict1 = dict()
print(my_dict, type(my_dict))
print(my_dict1, type(my_dict1))

# 定义带数据的字典
my_dict2 = {'name': 'Tom', 'age': 18, 1: ['hello', 'python'], 'like': ['敲代码', '黑客攻击']}
print(my_dict2)

# 访问value值 在字典中没有 下标 这个概念,使用key值访问对应的value值
print(my_dict2['age'])
print(my_dict2['like'][1])

# # 如果key不存在,报错
# print(my_dict2[3])

# my_dict.get(key)  如果key不存在返回None , 如果key存在 返回key对应的value值
print(my_dict2.get(3))   # key值不存在,返回值为 None
print(my_dict2.get(1))
print('_'*20)
# get 方法的补充
# my_dict.get(key, value)  如果key不存在, 返回书写的value数据值 , 如果key存在 返回字典中key对应的value值
print(my_dict2.get('like', '字典中没有这个数据值'))
print(my_dict2.get('Python', '字典中没有这个数据值'))

print(len(my_dict2))


#字典中添加和修改数据
my_dict3 = {'name': 'Tom'}
# 字典中添加和修改数据 使用key值进行添加和修改
# my_dict[key] = 数据值,如果key值存在,就是修改, key值不存在就是添加

my_dict3['name'] = 'java'
print(my_dict3)
my_dict3['like'] = ['敲代码', '黑客攻击']
print(my_dict3)

# 注意点 key值中 int中的  1  和  float 中的  1.0  代表的是一个数据
my_dict3[1] = 'int'
print(my_dict3)
my_dict3[1.0] = 'float'
print(my_dict3)

print('_'*20)

#字典中的数据删除
# 根据key值删除数据  格式: del my_dict[key]
my_dict4 = {'name': 'java', 'like': ['敲代码', '黑客攻击'], 1: 'float', 4: 45}
del my_dict4[1]
print(my_dict4)

# my_dict.pop(key)     也是根据key值 进行删除数据,返回值是删除的key对应的 value值
result = my_dict4.pop('name')
print(my_dict4)
print(result)

# my_dict.clear() 清空字典,不管有多少键对全部删除
my_dict4.clear()
print(my_dict4)

# del 字典名  直接将字典删除,不能再使用这个字典
del my_dict  # 后面不能在使用这个变量了 ,除非重新定义
# print(my_dict)   代码报错,变量未定义

print('_'*20)

#字典中的数据遍历
my_dict5 = {'name': 'Tom', 'age': 18, 'like': ['敲代码', '黑客攻击']}
# for 循环直接遍历字典,遍历的是字典的key值
for key in my_dict5:
    print(key, my_dict5[key])

# my_dict.keys() 获取字典中所有的key值,得到的类型是 dict_keys,该类型具有的特点是
# 1 可以使用list() 进行类型转换,即将其转换成列表类型
# 2 可以使用 for 循环进行遍历
result1 = my_dict5.keys()
print(result1, type(result1))
for key1 in result1:
    # print(key1)
    print(key1, my_dict5[key1])

print('_'*20)

# my_dict.values() 获取字典的所有value值  ,类型为 dict_values
# 1 可以使用list() 进行类型转换,即将其转换成列表类型
# 2 可以使用 for 循环进行遍历
result2 = my_dict5.values()
print(result2, type(result2))
for value in result2:
    print(value)
'''
for value in my_dict5.values():
    print(value)
'''
# my_dict.items() 获取字典中的所有的键值对,类型是 dict_items  , key,value组成元素类型
# 1 可以使用list() 进行类型转换,即将其转换成列表类型
# 2 可以使用 for 循环进行遍历
result3 = my_dict5.items()
print(result3, type(result3))
# ict_items([('name', 'Tom'), ('age', 18), ('like', ['敲代码', '黑客攻击'])]) <class 'dict_items'>
# 每一个键值对是一个元祖
for item in my_dict5.items():
    print(item[0], item[1])
    # print(item)

print('=*='*30)
# 拆包
for k, v in my_dict5.items():   # k 是元祖中的第一个数据, v 是元祖中的第二个数据
    print(k, v)






