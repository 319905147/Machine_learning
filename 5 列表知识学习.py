# 列表 是Python中的一种数据类型, 可以存放多个数据, 列表中的数据可以是任意类型
# 列表list 使用[]进行定义

#定义空列表
my_list = []
print(my_list, type(my_list))
my_list1 = list()   # 同样是空列表
print(my_list1, type(my_list1))

#定义带数据的列表,数据之间用 , 隔开
my_list2 = [1, 2.2, True, 'good']
print(my_list2, type(my_list2))

#求列表的数据个数 即列表的长度  len()
num = len(my_list2)
print(num)

#列表支持下标和切片操作
print(my_list2[1])  # 2.2
print(my_list2[1:3])    # 切片 得到是一个新的列表      [2.2, True]

#下标操作与字符串中不同的是, 字符串不能使用下标操作修改其中的数据, 但列表可以使用下标操作修改其中的数据
my_list2[0] = 20
print(my_list2)
my_list2[-1] = 'hello'
print(my_list2)


#列表的遍历
my_list3 = ['郭德纲', '于谦', '小岳岳', '孙越']
# for循环
for i in my_list3:  # i 可以是任意变量
    print(i)

print('*' * 30)

# while循环
j = 0   # j 表示下标
while j < len(my_list3):
    print(my_list3[j])
    j += 1

#列表添加数据
# 向列表中添加数据的方法,都是直接向原列表中添加, 不会返回新的列表
# my_list.append(数据) 向列表的尾部添加数据
my_list3.append('郭麒麟')
print(my_list3)
result = my_list3 .append('烧饼') # 不要这样书写
print(result)           # None 是一个关键字 表示空
print(my_list3)

# my_list.insert(下标, 数据)  在指定的下标位置进行添加
my_list3.insert(0, 'python')
print(my_list3)
# print(my_list3.insert(5, 'hello'))     不能这样书写, None

# my_list.extend(可迭代对象)  # str 列表, 会将可迭代对象中的数据逐个添加到列表中的末尾
my_list4 = ['郭德纲', '于谦', '小岳岳', '孙越']
my_list4.extend('hello')
print(my_list4)
my_list4.extend([1, 'python', 3, 4])
print(my_list4)


#列表的查询
# index()根据数据值,查找元素所在的下标,找到返回元素的下标,没有找到,程序报错
# 列表中没有find方法,只有index() 方法
num = my_list4.index('于谦')
print(num)
# num1 = my_list4.index('郭麒麟')
# print(num1)

# count() 统计出现的次数
num2 = my_list4.count('郭德纲')    # True 会被当做整数 1
print(num2)

# in /not in  判断是否存在 ,存在  true ,不存在 false   ; 一般和if 结合使用
num3 = '小岳岳' in my_list4
print(num3)

num5 = '小岳岳' not in my_list4
print(num5)

print('-'*10)
num4 = '郭麒麟' in my_list4
print(num4)

my_list5 = [1, 2, 3, 4, 5, 6]

#列表的删除
# remove(数据值) 根据元素数据值进行删除,直接在原列表中删除
my_list5.remove(4)
print(my_list5)
# my_list5.remove(4)  # 程序会报错,要删除的数据不存在

# 根据下标进行删除
# 1 pop(下标) 默认删除最后一个数据,返回删除的内容
num6 = my_list5.pop()
print(num6)
print(my_list5)
print('-'*10)

num7 = my_list5.pop(1)
print(num7)
print(my_list5)

# num8 = my_list5.pop(10)  # 删除了下标不存在的数据,会报错
print('-'*10)

# 2 del my_list[下标]
del my_list5[0]
print(my_list5)

# del my_list5[10] # 删除不存在的下标.会报错

#列表的排序和逆置,前提是列表中的数据类型是一样的
# my_list.sort() 直接在原列表中排序,默认是从小到大排序,即升序
my_list6 = [1, 72, 5, 97, 18, 47]
my_list6.sort()
print(my_list6)

print('-'*20)

my_list6.sort(reverse=True)  # 通过reverse=True,将列表从大到小进行排序,即降序
print(my_list6)

my_list6.sort(reverse=False)  # 通过reverse=True,将列表从小大小进行排序,即升序序
print(my_list6)
print('-'*20)

# 补充 sorted(my_list)   将列表升序,不会在原列表中排序,得到一个新的列表
my_list7 = [3, 5, 1, 67]
print(my_list7)
my_list8 = sorted(my_list7)
print(my_list8)

my_list9 = sorted(my_list7, reverse=True)
print(my_list9)
# 列表的逆置
my_list10 = ['a', 'b', 'c', 'd', 'e', 'f']
my_list11 = my_list10[::-1]     # 得到一个新的列表
print(my_list10)
print(my_list11)
print('/'*40)

# 在原列表中逆置 my_list.reverse()
my_list10.reverse()
print(my_list10)


#列表的嵌套
names = [['郭德纲', '郭麒麟'], ['岳云鹏', '孙越', '于谦'], ['孙悟空', '猪八戒', '唐三藏', '沙悟净']]
print(names[1])   # ['岳云鹏', '孙越', '于谦']
print(names[1][1])      # 孙越   (孙越是一个字符串可以使用下标)
print(names[1][1][1])      # 越

# 遍历
for i in names:
    print(i)    # 列表遍历
    for j in i:
        print(j)    #

print('-*-'*30)

#enumerate()
my_list12 = ['a', 'b', 'c', 'd', 'e', 'f']
# for i in my_list12:
#     print(i)


for i in my_list12:
    print(my_list12.index(i), i)   # 下标 ,数据值


# enumerate 将可迭代序列中元素所在的下标和具体元素数据组合在一块,变成元祖
for j in enumerate(my_list12):
    print(j)