# 列表推导式 为了快速生成一个列表
# 1 变量 = [列表数据的规则 for 临时变量 in xxx]
# 每循环一次,就会创建一个数据
my_list = [i for i in range(5)]
print(my_list)

my_list1 = ['hello' for i in range(5)]
print(my_list1)   # 每循环一次就向列表中添加一个 'hello'

my_list2 = [f'num:{i}' for i in my_list]
print(my_list2)

my_list3 = [i+i for i in range(5)]
print(my_list3)


# 2  变量 = [列表数据的规则 for 临时变量 in xxx if xxx]
# 每循环一次 并且if 条件为 TRUE ,就生成一个数据

my_list4 = [i for i in range(5) if i % 2 == 0]
print(my_list4)


# 3 变量 = [列表数据的规则 for 临时变量 in xxx for j in xxx]
# 第二个 for 循环  循环一次 ,就生成一个数据
my_list5 = [(i, j) for i in range(5) for j in range(3)]
print(my_list5)


# 补充 字典推导式
# 变量 = {生成字典的规则 for 临时变量 in xxx}
my_dict = {f'name{i}': i for i in range(3)}
print(my_dict)












