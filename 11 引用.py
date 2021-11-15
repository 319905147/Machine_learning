# 可以使用id() 查看变量的引用,可以将id值认为是内存地址的别名
# Python 中数据值得传递用的是引用
# 赋值运算符可以改变变量的引用

# 将数据10 存储到变量a 中, 本质将数据10 所在内存的引用地址保存到变量a 中
a = 10
b = a   # 将变量a中保存的引用地址给到b
print(a, b)  # 使用print函数打印变量 a 和 b 引用中存储的值
print(id(a), id(b))
a = 20
print(a, b)
print(id(a), id(b))


my_list = [1, 2, 3]  # 将列表的引用地址保存到变量my_list中
my_list1 = my_list   # 将my_list 变量中存储的引用地址给到my_list1
print(my_list, id(my_list))
print(my_list1, id(my_list1))

my_list.append(4)   # 想列表中添加数字 4 ,将数据4 的引用保存到列表中
print(my_list, id(my_list))
print(my_list1, id(my_list1))

my_list[2] = 5
print(my_list, id(my_list))
print(my_list1, id(my_list1))

# 类型的可变与不可变: 在不改变变量引用的前提下,能否改变变量引用中的引用的数据
# 如果能改变就是可变类型,如果不能改变就是不可变类型
# int float bool  str list tuple dict
# 不可变类型  int float  str  bool tuple
# 可变类型   list  dict


c = 10
d = 10
print(id(c), id(d))   # python 中的内存优化,对于不可变类型进行的

print('-'*20)

my_list2 = [1, 3, 4, 5]
my_list3 = [1, 3, 4, 5]
print(id(my_list2), id(my_list3))

print('='*20)

# 引用做函数参数传递
# 函数传参传递的也是引用
my_list4 = [1, 2, 3]   # 全局变量


def func1(e):
    e.append(4)


def func2():
    # 为啥不加global ,因为没有修改my_list4 中存的引用值
    my_list4.append(5)


func1(my_list4)
func2()
print(my_list4)













