# 列表排序,列表中的数据类型保持一致
my_list = [1, 2, 5, 9, 7]
my_list.sort()
print(my_list)


list1 = [{'name': 'd', 'age': 19}, {'name': 'b', 'age': 16},
         {'name': 'c', 'age': 20}, {'name': 'a', 'age': 16}]


"""
list1.sort()    # 程序报错 ,列表中的数据是字典类型,字典如何比较大小,程序不知道,需要我们告诉程序,如何对字典比较大小
print(list1)
"""
# 匿名函数的形参是列表中的每一个数据  (下行的 x )
list1.sort(key=lambda x: x['name'])
print(list1)
list1.sort(key=lambda x: x['age'])
print(list1)



list2 = ['a', 'bc', 'abc', 'def', 'ghl', 'python']  # 字符串默认可以排序 根据 ascll 码表排序
list2.sort()
print(list2)

# 需求根据 列表中字符串的长度,对列表进行排序
# list2.sort(key=len)
list2.sort(key=lambda x: len(x))
print(list2)

# sort(key= lambda 形参:(排序的规则1,排序的规则2...))
# 当第一个规则相同,则按照第二个规则排序

list1.sort(key=lambda x: (x['age'], x['name']), reverse=True)
print(list1)






